import asyncio
import datetime
import os
import ssl
import tempfile
import unittest
from unittest.mock import patch

import websockets
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import NameOID

from coinbase.websocket import WSClient, WSClientException


def _ignore_server_handshake_errors(loop, context):
    # the server side of a refused handshake is expected to fail
    if isinstance(context.get("exception"), (ConnectionResetError, ssl.SSLError)):
        return
    loop.default_exception_handler(context)


def _write_self_signed_cert(directory):
    key = ec.generate_private_key(ec.SECP256R1())
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
    now = datetime.datetime.now(datetime.timezone.utc)
    ski = x509.SubjectKeyIdentifier.from_public_key(key.public_key())
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(hours=1))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False
        )
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(ski, critical=False)
        .add_extension(
            x509.AuthorityKeyIdentifier.from_issuer_subject_key_identifier(ski),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )
    cert_path = os.path.join(directory, "cert.pem")
    key_path = os.path.join(directory, "key.pem")
    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open(key_path, "wb") as f:
        f.write(
            key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        )
    return cert_path, key_path


class WSTLSVerificationTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        asyncio.get_running_loop().set_exception_handler(
            _ignore_server_handshake_errors
        )
        self.tmp = tempfile.TemporaryDirectory()
        self.cert_path, key_path = _write_self_signed_cert(self.tmp.name)

        server_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        server_ctx.load_cert_chain(self.cert_path, key_path)

        async def handler(websocket, *_):
            async for message in websocket:
                await websocket.send(message)

        self.server = await websockets.serve(
            handler, "127.0.0.1", 0, ssl=server_ctx, logger=None
        )
        self.port = self.server.sockets[0].getsockname()[1]

    async def asyncTearDown(self):
        self.server.close()
        await self.server.wait_closed()
        self.tmp.cleanup()

    def _client(self, host, scheme="wss"):
        return WSClient(
            base_url=f"{scheme}://{host}:{self.port}",
            on_message=lambda _: None,
            retry=False,
        )

    async def test_rejects_untrusted_certificate(self):
        client = self._client("localhost")

        with self.assertRaises(WSClientException) as ctx:
            await client.open_async()

        self.assertIsInstance(ctx.exception.__cause__, ssl.SSLCertVerificationError)
        self.assertIsNone(client.websocket)

    async def test_uppercase_scheme_uses_tls(self):
        client = self._client("localhost", scheme="WSS")

        with self.assertRaises(WSClientException) as ctx:
            await client.open_async()

        self.assertIsInstance(ctx.exception.__cause__, ssl.SSLCertVerificationError)

    async def test_rejects_hostname_mismatch(self):
        # certificate is trusted but only valid for "localhost"
        client = self._client("127.0.0.1")

        with patch.dict(os.environ, {"SSL_CERT_FILE": self.cert_path}):
            with self.assertRaises(WSClientException) as ctx:
                await client.open_async()

        self.assertIsInstance(ctx.exception.__cause__, ssl.SSLCertVerificationError)
        self.assertIn("mismatch", str(ctx.exception.__cause__).lower())

    async def test_accepts_trusted_certificate(self):
        client = self._client("localhost")

        with patch.dict(os.environ, {"SSL_CERT_FILE": self.cert_path}):
            await client.open_async()

        try:
            self.assertIsNotNone(client.websocket)
        finally:
            await client.close_async()

from coinbase import jwt_generator


def build_cdp_jwt(api_key: str, api_secret: str) -> str:
    """Sign a CDP JWT to present at the gateway's public/auth endpoint.

    Reuses the existing jwt_generator, so ECDSA (ES256) and Ed25519 keys are both
    handled with the same auto-detection as the spot RESTClient. The token is the
    credential for the ``coinbase_cdp`` grant; the gateway validates its signature
    via Cloud API Keys and returns a short-lived Deribit access_token.

    Unlike the per-request REST JWT, no ``uri`` claim is set — public/auth presents
    the key itself rather than authorizing a single scoped request.

    :meta private:
    """
    return jwt_generator.build_jwt(api_key, api_secret)

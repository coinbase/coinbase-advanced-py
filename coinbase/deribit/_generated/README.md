# `coinbase/deribit/_generated/`

Generated code. **Do not hand-edit** — regenerate from the Deribit Retail specs.

Source specs (Coinbase Deribit Retail gateway, `drb.coinbase.com`):
- REST/RPC: `deribit_openapi.json` (OpenAPI 3.0) → request/response models + REST method stubs
- WebSocket: `deribit_asyncapi.json` (AsyncAPI 3.0) → subscription channel builders + notification payload models

Models are emitted in the SDK's existing `BaseResponse` idiom (see `coinbase/rest/types/`),
not a stock generator's attrs/httpx output, so they stay consistent with the rest of
the package. The hand-authored runtime (`auth/`, `ws_client.py`, `errors.py`, rate limiting,
write-safety) lives outside this directory and imports from it.

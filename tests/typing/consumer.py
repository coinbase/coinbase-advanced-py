from coinbase.jwt_generator import format_jwt_uri
from coinbase.rest import RESTClient

RESTClient(timeout=10)
RESTClient(timeout="ten")  # type: ignore[arg-type]

uri: str = format_jwt_uri("GET", "/path")
number: int = format_jwt_uri("GET", "/path")  # type: ignore[assignment]

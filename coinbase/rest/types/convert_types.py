from typing import Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import RatConvertTrade


# Create Convert Quote
class CreateConvertQuoteResponse(BaseResponse):
    def __init__(self, response: dict):
        if "trade" in response:
            self.trade: Optional[RatConvertTrade] = RatConvertTrade(
                **response.pop("trade")
            )
        super().__init__(**response)


# Get Convert Trade
class GetConvertTradeResponse(BaseResponse):
    def __init__(self, response: dict):
        if "trade" in response:
            self.trade: Optional[RatConvertTrade] = RatConvertTrade(
                **response.pop("trade")
            )
        super().__init__(**response)


# Commit Convert Trade
class CommitConvertTradeResponse(BaseResponse):
    def __init__(self, response: dict):
        if "trade" in response:
            self.trade: Optional[RatConvertTrade] = RatConvertTrade(
                **response.pop("trade")
            )
        super().__init__(**response)

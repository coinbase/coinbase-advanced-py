from typing import List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import Portfolio, PortfolioBreakdown


# List Portfolios
class ListPortfoliosResponse(BaseResponse):
    def __init__(self, response: dict):
        if "portfolios" in response:
            self.portfolios: Optional[List[Portfolio]] = [
                Portfolio(**portfolio) for portfolio in response.pop("portfolios")
            ]
        super().__init__(**response)


# Create Portfolio
class CreatePortfolioResponse(BaseResponse):
    def __init__(self, response: dict):
        if "portfolio" in response:
            self.portfolio: Optional[Portfolio] = Portfolio(**response.pop("portfolio"))
        super().__init__(**response)


# Move Portfolio Funds
class MovePortfolioFundsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "source_portfolio_uuid" in response:
            self.source_portfolio_uuid: Optional[str] = response.pop(
                "source_portfolio_uuid"
            )
        if "target_portfolio_uuid" in response:
            self.target_portfolio_uuid: Optional[str] = response.pop(
                "target_portfolio_uuid"
            )
        super().__init__(**response)


# Get Portfolio Breakdown
class GetPortfolioBreakdownResponse(BaseResponse):
    def __init__(self, response: dict):
        if "breakdown" in response:
            self.breakdown: Optional[PortfolioBreakdown] = PortfolioBreakdown(
                **response.pop("breakdown")
            )
        super().__init__(**response)


# Delete Portfolio
class DeletePortfolioResponse(BaseResponse):
    def __init__(self, response: dict):
        super().__init__(**response)


# Edit Portfolio
class EditPortfolioResponse(BaseResponse):
    def __init__(self, response: dict):
        if "portfolio" in response:
            self.portfolio: Optional[Portfolio] = Portfolio(**response.pop("portfolio"))
        super().__init__(**response)

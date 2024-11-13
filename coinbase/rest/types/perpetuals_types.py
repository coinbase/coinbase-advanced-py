from typing import List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import (
    PerpetualPortfolio,
    PortfolioBalance,
    PortfolioSummary,
    Position,
    PositionSummary,
)


# Allocate Portfolio
class AllocatePortfolioResponse(BaseResponse):
    def __init__(self, response: dict):
        super().__init__(**response)


# Get Perpetuals Portfolio Summary
class GetPerpetualsPortfolioSummaryResponse(BaseResponse):
    def __init__(self, response: dict):
        if "portfolios" in response:
            self.portfolios: Optional[List[PerpetualPortfolio]] = [
                PerpetualPortfolio(**portfolio)
                for portfolio in response.pop("portfolios")
            ]
        if "summary" in response:
            self.summary: Optional[PortfolioSummary] = PortfolioSummary(
                **response.pop("summary")
            )
        super().__init__(**response)


# List Perpetuals Positions
class ListPerpetualsPositionsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "positions" in response:
            self.positions: Optional[List[Position]] = [
                Position(**pos) for pos in response.pop("positions")
            ]
        if "summary" in response:
            self.summary: Optional[PositionSummary] = PositionSummary(
                **response.pop("summary")
            )
        super().__init__(**response)


# Get Perpetuals Position
class GetPerpetualsPositionResponse(BaseResponse):
    def __init__(self, response: dict):
        if "position" in response:
            self.position: Optional[Position] = Position(**response.pop("position"))
        super().__init__(**response)


# Get Portfolio Balances
class GetPortfolioBalancesResponse(BaseResponse):
    def __init__(self, response: dict):
        if "portfolio_balances" in response:
            self.portfolio_balances: Optional[List[PortfolioBalance]] = [
                PortfolioBalance(**balance)
                for balance in response.pop("portfolio_balances")
            ]
        super().__init__(**response)


# Opt In or Out of Multi Asset Collateral
class OptInOutMultiAssetCollateralResponse(BaseResponse):
    def __init__(self, response: dict):
        if "cross_collateral_enabled" in response:
            self.cross_collateral_enabled: Optional[bool] = response.pop(
                "cross_collateral_enabled"
            )
        super().__init__(**response)

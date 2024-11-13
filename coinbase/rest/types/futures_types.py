from typing import Any, Dict, List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import (
    FCMBalanceSummary,
    FCMPosition,
    FCMSweep,
    IntradayMarginSetting,
)


# Get Futures Balance Summary
class GetFuturesBalanceSummaryResponse(BaseResponse):
    def __init__(self, response: dict):
        if "balance_summary" in response:
            self.balance_summary: Optional[FCMBalanceSummary] = FCMBalanceSummary(
                **response.pop("balance_summary")
            )
        super().__init__(**response)


# List Futures Positions
class ListFuturesPositionsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "positions" in response:
            self.positions: Optional[List[FCMPosition]] = [
                FCMPosition(**position) for position in response.pop("positions")
            ]
        super().__init__(**response)


# Get Futures Position
class GetFuturesPositionResponse(BaseResponse):
    def __init__(self, response: dict):
        if "position" in response:
            self.position: Optional[FCMPosition] = FCMPosition(
                **response.pop("position")
            )
        super().__init__(**response)


# Schedule Futures Sweep
class ScheduleFuturesSweepResponse(BaseResponse):
    def __init__(self, response: dict):
        if "success" in response:
            self.success: Optional[bool] = response.pop("success")
        super().__init__(**response)


# List Futures Sweeps
class ListFuturesSweepsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "sweeps" in response:
            self.sweeps: List[FCMSweep] = [
                FCMSweep(**sweep) for sweep in response.pop("sweeps")
            ]
        super().__init__(**response)


# Cancel Pending Futures Sweep
class CancelPendingFuturesSweepResponse(BaseResponse):
    def __init__(self, response: dict):
        if "success" in response:
            self.success: Optional[bool] = response.pop("success")
        super().__init__(**response)


# Get Intraday Margin Setting
class GetIntradayMarginSettingResponse(BaseResponse):
    def __init__(self, response: dict):
        if "setting" in response:
            self.setting: Optional[IntradayMarginSetting] = response.pop("setting")
        super().__init__(**response)


# Get Current Margin Window
class GetCurrentMarginWindowResponse(BaseResponse):
    def __init__(self, response: dict):
        if "margin_window" in response:
            self.margin_window: Optional[Dict[str, Any]] = response.pop("margin_window")
        if "is_intraday_margin_killswitch_enabled" in response:
            self.is_intraday_margin_killswitch_enabled: Optional[bool] = response.pop(
                "is_intraday_margin_killswitch_enabled"
            )
        if "is_intraday_margin_enrollment_killswitch_enabled" in response:
            self.is_intraday_margin_enrollment_killswitch_enabled: Optional[bool] = (
                response.pop("is_intraday_margin_enrollment_killswitch_enabled")
            )
        super().__init__(**response)


# Set Intraday Margin Setting
class SetIntradayMarginSettingResponse(BaseResponse):
    def __init__(self, response: dict):
        super().__init__(**response)

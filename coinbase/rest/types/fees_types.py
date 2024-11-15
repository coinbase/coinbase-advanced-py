from typing import Any, Dict, Optional

from coinbase.rest.types.base_response import BaseResponse


# Get Transaction Summary
class GetTransactionSummaryResponse(BaseResponse):
    def __init__(self, response: dict):
        if "total_volume" in response:
            self.total_volume: int = response.pop("total_volume", 0.0)
        if "total_fees" in response:
            self.total_fees: int = response.pop("total_fees", 0.0)
        if "fee_tier" in response:
            self.fee_tier: Dict[str, Any] = response.pop("fee_tier")
        if "margin_rate" in response:
            self.margin_rate: Optional[Dict[str, Any]] = response.pop("margin_rate")
        if "goods_and_services_tax" in response:
            self.goods_and_services_tax: Optional[Dict[str, Any]] = response.pop(
                "goods_and_services_tax"
            )
        if "advanced_trade_only_volumes" in response:
            self.advanced_trade_only_volumes: Optional[int] = response.pop(
                "advanced_trade_only_volumes"
            )
        if "advanced_trade_only_fees" in response:
            self.advanced_trade_only_fees: Optional[int] = response.pop(
                "advanced_trade_only_fees"
            )
        if "coinbase_pro_volume" in response:  # deprecated
            self.coinbase_pro_volume: Optional[int] = response.pop(
                "coinbase_pro_volume"
            )
        if "coinbase_pro_fees" in response:  # deprecated
            self.coinbase_pro_fees: Optional[int] = response.pop("coinbase_pro_fees")
        if "total_balance" in response:
            self.total_balance: Optional[str] = response.pop("total_balance")
        if "has_promo_fee" in response:
            self.has_promo_fee: Optional[bool] = response.pop("has_promo_fee")
        super().__init__(**response)

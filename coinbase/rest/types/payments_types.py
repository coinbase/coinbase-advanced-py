from typing import List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import PaymentMethod


# List Payment Methods
class ListPaymentMethodsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "payment_methods" in response:
            self.payment_methods: Optional[List[PaymentMethod]] = [
                PaymentMethod(**method) for method in response.pop("payment_methods")
            ]

        super().__init__(**response)


# Get Payment Method
class GetPaymentMethodResponse(BaseResponse):
    def __init__(self, response: dict):
        if "payment_method" in response:
            self.payment_method: Optional[PaymentMethod] = PaymentMethod(
                **response.pop("payment_method")
            )
        super().__init__(**response)

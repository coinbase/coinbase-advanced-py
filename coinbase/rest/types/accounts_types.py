from typing import List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import Account


# Get Account
class GetAccountResponse(BaseResponse):
    def __init__(self, response: dict):
        if "account" in response:
            self.account: Optional[Account] = Account(**(response.pop("account")))
        super().__init__(**response)


# List Accounts
class ListAccountsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "accounts" in response:
            self.accounts: Optional[List[Account]] = [
                Account(**account) for account in response.pop("accounts")
            ]
        if "has_next" in response:
            self.has_next: Optional[bool] = response.pop("has_next")
        if "cursor" in response:
            self.cursor: Optional[str] = response.pop("cursor")
        if "size" in response:
            self.size: Optional[int] = response.pop("size")
        super().__init__(**response)

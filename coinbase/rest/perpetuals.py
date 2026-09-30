from coinbase.constants import API_PREFIX
from coinbase.rest._intx_cutover import intx_migration_hint
from coinbase.rest.types.perpetuals_types import (
    AllocatePortfolioResponse,
    GetPerpetualsPortfolioSummaryResponse,
    GetPerpetualsPositionResponse,
    GetPortfolioBalancesResponse,
    ListPerpetualsPositionsResponse,
    OptInOutMultiAssetCollateralResponse,
)


def allocate_portfolio(
    self, portfolio_uuid: str, symbol: str, amount: str, currency: str, **kwargs
) -> AllocatePortfolioResponse:
    """
    **Allocate Portfolio**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/intx/allocate

    __________

    **Description:**

    Allocate more funds to an isolated position in your Perpetuals portfolio.

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Isolated margin lives in a managed subaccount:
    use ``private_submit_transfer_between_subaccounts`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `Allocate Portfolio
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio>`_
    """
    endpoint = f"{API_PREFIX}/intx/allocate"

    data = {
        "portfolio_uuid": portfolio_uuid,
        "symbol": symbol,
        "amount": amount,
        "currency": currency,
    }

    with intx_migration_hint(
        "allocate_portfolio", "private_submit_transfer_between_subaccounts"
    ):
        return AllocatePortfolioResponse(self.post(endpoint, data=data, **kwargs))


def get_perps_portfolio_summary(
    self, portfolio_uuid: str, **kwargs
) -> GetPerpetualsPortfolioSummaryResponse:
    """
    **Get Perpetuals Portfolio Summary**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}

    __________

    **Description:**

    Get a summary of your Perpetuals portfolio.

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Use ``private_get_account_summary`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `Get Perpetuals Portfolio Summary
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary>`_
    """
    endpoint = f"{API_PREFIX}/intx/portfolio/{portfolio_uuid}"

    with intx_migration_hint(
        "get_perps_portfolio_summary", "private_get_account_summary"
    ):
        return GetPerpetualsPortfolioSummaryResponse(self.get(endpoint, **kwargs))


def list_perps_positions(
    self, portfolio_uuid: str, **kwargs
) -> ListPerpetualsPositionsResponse:
    """
    **List Perpetuals Positions**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}

    __________

    **Description:**

    Get a list of open positions in your Perpetuals portfolio.

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Use ``private_get_positions`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `List Perpetuals Positions
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/list-perpetuals-positions>`_
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}"

    with intx_migration_hint("list_perps_positions", "private_get_positions"):
        return ListPerpetualsPositionsResponse(self.get(endpoint, **kwargs))


def get_perps_position(
    self, portfolio_uuid: str, symbol: str, **kwargs
) -> GetPerpetualsPositionResponse:
    """
    **Get Perpetuals Position**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}/{symbol}

    __________

    **Description:**

    Get a specific open position in your Perpetuals portfolio

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Use ``private_get_position`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `Get Perpetuals Positions
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-position>`_
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}/{symbol}"

    with intx_migration_hint("get_perps_position", "private_get_position"):
        return GetPerpetualsPositionResponse(self.get(endpoint, **kwargs))


def get_perps_portfolio_balances(
    self, portfolio_uuid: str, **kwargs
) -> GetPortfolioBalancesResponse:
    """
    **Get Portfolio Balances**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}

    __________

    **Description:**

    Get a list of asset balances on Intx for a given Portfolio

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Use ``private_get_account_summaries`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `Get Portfolio Balances
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances>`_
    """
    endpoint = f"{API_PREFIX}/intx/balances/{portfolio_uuid}"

    with intx_migration_hint(
        "get_perps_portfolio_balances", "private_get_account_summaries"
    ):
        return GetPortfolioBalancesResponse(self.get(endpoint, **kwargs))


def opt_in_or_out_multi_asset_collateral(
    self, portfolio_uuid: str, multi_asset_collateral_enabled: bool, **kwargs
) -> OptInOutMultiAssetCollateralResponse:
    """
    **Opt In or Out of Multi Asset Collateral**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral

    __________

    **Description:**

    Enable or Disable Multi Asset Collateral for a given Portfolio.

    __________

    **Global Derivatives:** From October 1, 2026, Global Derivatives run on the
    Deribit-powered gateway instead of INTX.
    The request is still sent. If the server rejects it, the SDK logs a migration
    hint and re-raises the ``HTTPError``. Use ``private_change_margin_model`` on
    ``coinbase.deribit.DeribitRetailClient`` instead.

    __________

    **Read more on the official documentation:** `Opt In or Out of Multi Asset Collateral
    <https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out>`_
    """
    endpoint = f"{API_PREFIX}/intx/multi_asset_collateral"

    data = {
        "portfolio_uuid": portfolio_uuid,
        "multi_asset_collateral_enabled": multi_asset_collateral_enabled,
    }

    with intx_migration_hint(
        "opt_in_or_out_multi_asset_collateral", "private_change_margin_model"
    ):
        return OptInOutMultiAssetCollateralResponse(
            self.post(endpoint, data=data, **kwargs)
        )

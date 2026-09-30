"""GENERATED from the Deribit Retail OpenAPI spec — do not edit."""

from coinbase.deribit._generated import models


class GeneratedRESTMixin:
    """RPC methods served on both REST and WebSocket. Mixed into both
    clients, which implement ``_rpc(method, params, model_cls)``."""

    def private_buy(
        self,
        instrument_name,
        *,
        amount=None,
        contracts=None,
        type=None,
        label=None,
        price=None,
        time_in_force=None,
        display_amount=None,
        post_only=None,
        reject_post_only=None,
        reduce_only=None,
        trigger_price=None,
        trigger_offset=None,
        trigger=None,
        advanced=None,
        mmp=None,
        valid_until=None,
        linked_order_type=None,
        trigger_fill_condition=None,
        otoco_config=None,
        isolated=None,
        allocated_margin=None
    ):
        """private/buy"""
        params = {
            "instrument_name": instrument_name,
            "amount": amount,
            "contracts": contracts,
            "type": type,
            "label": label,
            "price": price,
            "time_in_force": time_in_force,
            "display_amount": display_amount,
            "post_only": post_only,
            "reject_post_only": reject_post_only,
            "reduce_only": reduce_only,
            "trigger_price": trigger_price,
            "trigger_offset": trigger_offset,
            "trigger": trigger,
            "advanced": advanced,
            "mmp": mmp,
            "valid_until": valid_until,
            "linked_order_type": linked_order_type,
            "trigger_fill_condition": trigger_fill_condition,
            "otoco_config": otoco_config,
            "isolated": isolated,
            "allocated_margin": allocated_margin,
        }
        return self._rpc("private/buy", params, models.PrivateBuyAndSellResponse)

    def private_cancel(self, order_id, *, isolated=None):
        """private/cancel"""
        params = {"order_id": order_id, "isolated": isolated}
        return self._rpc("private/cancel", params, models.PrivateCancelResponse)

    def private_cancel_all(
        self, *, detailed=None, freeze_quotes=None, include_isolated=None
    ):
        """private/cancel_all"""
        params = {
            "detailed": detailed,
            "freeze_quotes": freeze_quotes,
            "include_isolated": include_isolated,
        }
        return self._rpc("private/cancel_all", params, models.PrivateCancelAllResponse)

    def private_cancel_all_by_currency(
        self,
        currency,
        *,
        kind=None,
        type=None,
        detailed=None,
        freeze_quotes=None,
        include_isolated=None
    ):
        """private/cancel_all_by_currency"""
        params = {
            "currency": currency,
            "kind": kind,
            "type": type,
            "detailed": detailed,
            "freeze_quotes": freeze_quotes,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/cancel_all_by_currency", params, models.PrivateCancelAllResponse
        )

    def private_cancel_all_by_currency_pair(
        self, currency_pair, *, kind=None, type=None, detailed=None, freeze_quotes=None
    ):
        """private/cancel_all_by_currency_pair"""
        params = {
            "currency_pair": currency_pair,
            "kind": kind,
            "type": type,
            "detailed": detailed,
            "freeze_quotes": freeze_quotes,
        }
        return self._rpc(
            "private/cancel_all_by_currency_pair",
            params,
            models.PrivateCancelAllResponse,
        )

    def private_cancel_all_by_instrument(
        self,
        instrument_name,
        *,
        type=None,
        detailed=None,
        include_combos=None,
        freeze_quotes=None,
        include_isolated=None
    ):
        """private/cancel_all_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "type": type,
            "detailed": detailed,
            "include_combos": include_combos,
            "freeze_quotes": freeze_quotes,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/cancel_all_by_instrument", params, models.PrivateCancelAllResponse
        )

    def private_cancel_all_by_kind_or_type(
        self, currency, *, kind=None, type=None, detailed=None, freeze_quotes=None
    ):
        """private/cancel_all_by_kind_or_type"""
        params = {
            "currency": currency,
            "kind": kind,
            "type": type,
            "detailed": detailed,
            "freeze_quotes": freeze_quotes,
        }
        return self._rpc(
            "private/cancel_all_by_kind_or_type",
            params,
            models.PrivateCancelAllResponse,
        )

    def private_cancel_by_label(self, label, *, currency=None, include_isolated=None):
        """private/cancel_by_label"""
        params = {
            "label": label,
            "currency": currency,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/cancel_by_label", params, models.PrivateCancelAllResponse
        )

    def private_change_margin_model(self, margin_model, *, user_id=None, dry_run=None):
        """private/change_margin_model"""
        params = {"margin_model": margin_model, "user_id": user_id, "dry_run": dry_run}
        return self._rpc(
            "private/change_margin_model",
            params,
            models.PrivateChangeMarginModelResponse,
        )

    def private_close_position(
        self, instrument_name, type, *, price=None, isolated=None
    ):
        """private/close_position"""
        params = {
            "instrument_name": instrument_name,
            "type": type,
            "price": price,
            "isolated": isolated,
        }
        return self._rpc(
            "private/close_position", params, models.PrivateBuyAndSellResponse
        )

    def private_create_combo(self, trades):
        """private/create_combo"""
        params = {"trades": trades}
        return self._rpc(
            "private/create_combo", params, models.PrivateCreateComboResponse
        )

    def private_edit(
        self,
        order_id,
        *,
        amount=None,
        contracts=None,
        price=None,
        post_only=None,
        reduce_only=None,
        reject_post_only=None,
        advanced=None,
        trigger_price=None,
        trigger_offset=None,
        mmp=None,
        valid_until=None,
        display_amount=None,
        isolated=None,
        allocated_margin=None
    ):
        """private/edit"""
        params = {
            "order_id": order_id,
            "amount": amount,
            "contracts": contracts,
            "price": price,
            "post_only": post_only,
            "reduce_only": reduce_only,
            "reject_post_only": reject_post_only,
            "advanced": advanced,
            "trigger_price": trigger_price,
            "trigger_offset": trigger_offset,
            "mmp": mmp,
            "valid_until": valid_until,
            "display_amount": display_amount,
            "isolated": isolated,
            "allocated_margin": allocated_margin,
        }
        return self._rpc("private/edit", params, models.PrivateEditResponse)

    def private_edit_by_label(
        self,
        instrument_name,
        *,
        label=None,
        amount=None,
        contracts=None,
        price=None,
        post_only=None,
        reduce_only=None,
        reject_post_only=None,
        advanced=None,
        trigger_price=None,
        mmp=None,
        valid_until=None,
        isolated=None,
        allocated_margin=None
    ):
        """private/edit_by_label"""
        params = {
            "instrument_name": instrument_name,
            "label": label,
            "amount": amount,
            "contracts": contracts,
            "price": price,
            "post_only": post_only,
            "reduce_only": reduce_only,
            "reject_post_only": reject_post_only,
            "advanced": advanced,
            "trigger_price": trigger_price,
            "mmp": mmp,
            "valid_until": valid_until,
            "isolated": isolated,
            "allocated_margin": allocated_margin,
        }
        return self._rpc("private/edit_by_label", params, models.PrivateEditResponse)

    def private_get_account_summaries(
        self, *, subaccount_id=None, extended=None, include_isolated=None
    ):
        """private/get_account_summaries"""
        params = {
            "subaccount_id": subaccount_id,
            "extended": extended,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_account_summaries",
            params,
            models.PrivateAccountSummariesResponse,
        )

    def private_get_account_summary(
        self, currency, *, subaccount_id=None, extended=None
    ):
        """private/get_account_summary"""
        params = {
            "currency": currency,
            "subaccount_id": subaccount_id,
            "extended": extended,
        }
        return self._rpc(
            "private/get_account_summary", params, models.PrivateAccountResponse
        )

    def private_get_broker_trade_requests(self):
        """private/get_broker_trade_requests"""
        params = {}
        return self._rpc(
            "private/get_broker_trade_requests",
            params,
            models.PrivateGetBrokerTradeRequestsResponse,
        )

    def private_get_broker_trades(
        self, *, currency=None, count=None, start_id=None, end_id=None
    ):
        """private/get_broker_trades"""
        params = {
            "currency": currency,
            "count": count,
            "start_id": start_id,
            "end_id": end_id,
        }
        return self._rpc(
            "private/get_broker_trades", params, models.PrivateGetBrokerTradesResponse
        )

    def private_get_leg_prices(self, legs, price):
        """private/get_leg_prices"""
        params = {"legs": legs, "price": price}
        return self._rpc(
            "private/get_leg_prices", params, models.PrivateGetLegPricesResponse
        )

    def private_get_leverage(
        self, *, instrument_name=None, subaccount_id=None, isolated=None
    ):
        """private/get_leverage"""
        params = {
            "instrument_name": instrument_name,
            "subaccount_id": subaccount_id,
            "isolated": isolated,
        }
        return self._rpc(
            "private/get_leverage", params, models.PrivateGetLeverageResponse
        )

    def private_get_margins(self, instrument_name, amount, price, *, isolated=None):
        """private/get_margins"""
        params = {
            "instrument_name": instrument_name,
            "amount": amount,
            "price": price,
            "isolated": isolated,
        }
        return self._rpc(
            "private/get_margins", params, models.PrivateGetMarginsResponse
        )

    def private_get_max_order_size(
        self,
        instrument_name,
        *,
        subaccount_id=None,
        isolated=None,
        leverage=None,
        taker_fee_rate=None,
        price=None
    ):
        """private/get_max_order_size"""
        params = {
            "instrument_name": instrument_name,
            "subaccount_id": subaccount_id,
            "isolated": isolated,
            "leverage": leverage,
            "taker_fee_rate": taker_fee_rate,
            "price": price,
        }
        return self._rpc(
            "private/get_max_order_size", params, models.PrivateGetMaxOrderSizeResponse
        )

    def private_get_open_orders(
        self, *, kind=None, type=None, include_isolated=None, subaccount_id=None
    ):
        """private/get_open_orders"""
        params = {
            "kind": kind,
            "type": type,
            "include_isolated": include_isolated,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_open_orders", params, models.PrivateGetOpenOrdersResponse
        )

    def private_get_open_orders_by_currency(self, currency, *, kind=None, type=None):
        """private/get_open_orders_by_currency"""
        params = {"currency": currency, "kind": kind, "type": type}
        return self._rpc(
            "private/get_open_orders_by_currency",
            params,
            models.PrivateGetOpenOrdersResponse,
        )

    def private_get_open_orders_by_instrument(self, instrument_name, *, type=None):
        """private/get_open_orders_by_instrument"""
        params = {"instrument_name": instrument_name, "type": type}
        return self._rpc(
            "private/get_open_orders_by_instrument",
            params,
            models.PrivateGetOpenOrdersResponse,
        )

    def private_get_open_orders_by_label(self, currency, label):
        """private/get_open_orders_by_label"""
        params = {"currency": currency, "label": label}
        return self._rpc(
            "private/get_open_orders_by_label",
            params,
            models.PrivateGetOpenOrdersResponse,
        )

    def private_get_order_history_by_currency(
        self,
        currency,
        *,
        kind=None,
        count=None,
        offset=None,
        include_old=None,
        include_unfilled=None,
        with_continuation=None,
        continuation=None,
        historical=None,
        subaccount_id=None
    ):
        """private/get_order_history_by_currency"""
        params = {
            "currency": currency,
            "kind": kind,
            "count": count,
            "offset": offset,
            "include_old": include_old,
            "include_unfilled": include_unfilled,
            "with_continuation": with_continuation,
            "continuation": continuation,
            "historical": historical,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_order_history_by_currency",
            params,
            models.PrivateGetOrderHistoryResponse,
        )

    def private_get_order_history_by_instrument(
        self,
        instrument_name,
        *,
        count=None,
        offset=None,
        include_old=None,
        include_unfilled=None,
        with_continuation=None,
        continuation=None,
        historical=None
    ):
        """private/get_order_history_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "count": count,
            "offset": offset,
            "include_old": include_old,
            "include_unfilled": include_unfilled,
            "with_continuation": with_continuation,
            "continuation": continuation,
            "historical": historical,
        }
        return self._rpc(
            "private/get_order_history_by_instrument",
            params,
            models.PrivateGetOrderHistoryResponse,
        )

    def private_get_order_margin_by_ids(self, ids, *, isolated=None):
        """private/get_order_margin_by_ids"""
        params = {"ids": ids, "isolated": isolated}
        return self._rpc(
            "private/get_order_margin_by_ids",
            params,
            models.PrivateGetOrderMarginByIdsResponse,
        )

    def private_get_order_state(self, order_id, *, isolated=None):
        """private/get_order_state"""
        params = {"order_id": order_id, "isolated": isolated}
        return self._rpc(
            "private/get_order_state", params, models.PrivateGetOrderStateResponse
        )

    def private_get_order_state_by_label(
        self, currency, label, *, include_isolated=None
    ):
        """private/get_order_state_by_label"""
        params = {
            "currency": currency,
            "label": label,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_order_state_by_label",
            params,
            models.PrivateGetOrderStateByLabelResponse,
        )

    def private_get_pme_params(self, currency):
        """private/get_pme_params"""
        params = {"currency": currency}
        return self._rpc(
            "private/get_pme_params", params, models.PrivatePmeParamsResponse
        )

    def private_get_position(self, instrument_name, *, include_isolated=None):
        """private/get_position"""
        params = {
            "instrument_name": instrument_name,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_position", params, models.PrivateGetPositionResponse
        )

    def private_get_positions(
        self, *, currency=None, kind=None, subaccount_id=None, include_isolated=None
    ):
        """private/get_positions"""
        params = {
            "currency": currency,
            "kind": kind,
            "subaccount_id": subaccount_id,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_positions", params, models.PrivateGetPositionsResponse
        )

    def private_get_risk_profile(self):
        """private/get_risk_profile"""
        params = {}
        return self._rpc(
            "private/get_risk_profile", params, models.PrivateGetRiskProfileResponse
        )

    def private_get_settlement_history_by_currency(
        self,
        currency,
        *,
        type=None,
        count=None,
        continuation=None,
        search_start_timestamp=None,
        subaccount_id=None
    ):
        """private/get_settlement_history_by_currency"""
        params = {
            "currency": currency,
            "type": type,
            "count": count,
            "continuation": continuation,
            "search_start_timestamp": search_start_timestamp,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_settlement_history_by_currency",
            params,
            models.PrivateSettlementResponse,
        )

    def private_get_settlement_history_by_instrument(
        self,
        instrument_name,
        *,
        type=None,
        count=None,
        continuation=None,
        search_start_timestamp=None
    ):
        """private/get_settlement_history_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "type": type,
            "count": count,
            "continuation": continuation,
            "search_start_timestamp": search_start_timestamp,
        }
        return self._rpc(
            "private/get_settlement_history_by_instrument",
            params,
            models.PrivateSettlementResponse,
        )

    def private_get_subaccounts(self, *, with_portfolio=None, include_isolated=None):
        """private/get_subaccounts"""
        params = {
            "with_portfolio": with_portfolio,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_subaccounts", params, models.PrivateGetSubaccountsResponse
        )

    def private_get_subaccounts_details(
        self, currency, *, with_open_orders=None, include_isolated=None
    ):
        """private/get_subaccounts_details"""
        params = {
            "currency": currency,
            "with_open_orders": with_open_orders,
            "include_isolated": include_isolated,
        }
        return self._rpc(
            "private/get_subaccounts_details",
            params,
            models.PrivateGetSubaccountsDetailsResponse,
        )

    def private_get_trading_limits(self, currency):
        """private/get_trading_limits"""
        params = {"currency": currency}
        return self._rpc(
            "private/get_trading_limits", params, models.PrivateGetTradingLimitsResponse
        )

    def private_get_transaction_log(
        self,
        currency,
        start_timestamp,
        end_timestamp,
        *,
        query=None,
        count=None,
        subaccount_id=None,
        continuation=None
    ):
        """private/get_transaction_log"""
        params = {
            "currency": currency,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "query": query,
            "count": count,
            "subaccount_id": subaccount_id,
            "continuation": continuation,
        }
        return self._rpc(
            "private/get_transaction_log",
            params,
            models.PrivateGetTransactionLogResponse,
        )

    def private_get_trigger_order_history(
        self, currency, *, instrument_name=None, count=None, continuation=None
    ):
        """private/get_trigger_order_history"""
        params = {
            "currency": currency,
            "instrument_name": instrument_name,
            "count": count,
            "continuation": continuation,
        }
        return self._rpc(
            "private/get_trigger_order_history",
            params,
            models.PrivateGetTriggerOrderHistoryResponse,
        )

    def private_get_user_locks(self):
        """private/get_user_locks"""
        params = {}
        return self._rpc(
            "private/get_user_locks", params, models.PrivateGetUserLocksResponse
        )

    def private_get_user_trades_by_currency(
        self,
        currency,
        *,
        kind=None,
        start_id=None,
        end_id=None,
        count=None,
        start_timestamp=None,
        end_timestamp=None,
        sorting=None,
        historical=None,
        subaccount_id=None
    ):
        """private/get_user_trades_by_currency"""
        params = {
            "currency": currency,
            "kind": kind,
            "start_id": start_id,
            "end_id": end_id,
            "count": count,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "sorting": sorting,
            "historical": historical,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_user_trades_by_currency",
            params,
            models.PrivateGetUserTradesHistoryResponse,
        )

    def private_get_user_trades_by_currency_and_time(
        self,
        currency,
        start_timestamp,
        end_timestamp,
        *,
        kind=None,
        count=None,
        sorting=None,
        historical=None,
        subaccount_id=None
    ):
        """private/get_user_trades_by_currency_and_time"""
        params = {
            "currency": currency,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "kind": kind,
            "count": count,
            "sorting": sorting,
            "historical": historical,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_user_trades_by_currency_and_time",
            params,
            models.PrivateGetUserTradesHistoryResponse,
        )

    def private_get_user_trades_by_instrument(
        self,
        instrument_name,
        *,
        start_seq=None,
        end_seq=None,
        count=None,
        start_timestamp=None,
        end_timestamp=None,
        historical=None,
        sorting=None,
        subaccount_id=None
    ):
        """private/get_user_trades_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "start_seq": start_seq,
            "end_seq": end_seq,
            "count": count,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "historical": historical,
            "sorting": sorting,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_user_trades_by_instrument",
            params,
            models.PrivateGetUserTradesHistoryResponse,
        )

    def private_get_user_trades_by_instrument_and_time(
        self,
        instrument_name,
        start_timestamp,
        end_timestamp,
        *,
        count=None,
        sorting=None,
        historical=None,
        subaccount_id=None
    ):
        """private/get_user_trades_by_instrument_and_time"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count": count,
            "sorting": sorting,
            "historical": historical,
            "subaccount_id": subaccount_id,
        }
        return self._rpc(
            "private/get_user_trades_by_instrument_and_time",
            params,
            models.PrivateGetUserTradesHistoryResponse,
        )

    def private_get_user_trades_by_order(
        self,
        order_id,
        *,
        sorting=None,
        historical=None,
        subaccount_id=None,
        isolated=None
    ):
        """private/get_user_trades_by_order"""
        params = {
            "order_id": order_id,
            "sorting": sorting,
            "historical": historical,
            "subaccount_id": subaccount_id,
            "isolated": isolated,
        }
        return self._rpc(
            "private/get_user_trades_by_order",
            params,
            models.PrivateGetUserTradesByOrderResponse,
        )

    def private_pme_simulate(
        self, currency, *, add_positions=None, simulated_positions=None
    ):
        """private/pme/simulate"""
        params = {
            "currency": currency,
            "add_positions": add_positions,
            "simulated_positions": simulated_positions,
        }
        return self._rpc(
            "private/pme/simulate", params, models.PrivatePmeSimulateResponse
        )

    def private_sell(
        self,
        instrument_name,
        *,
        amount=None,
        contracts=None,
        type=None,
        label=None,
        price=None,
        time_in_force=None,
        display_amount=None,
        post_only=None,
        reject_post_only=None,
        reduce_only=None,
        trigger_price=None,
        trigger_offset=None,
        trigger=None,
        advanced=None,
        mmp=None,
        valid_until=None,
        linked_order_type=None,
        trigger_fill_condition=None,
        otoco_config=None,
        isolated=None,
        allocated_margin=None
    ):
        """private/sell"""
        params = {
            "instrument_name": instrument_name,
            "amount": amount,
            "contracts": contracts,
            "type": type,
            "label": label,
            "price": price,
            "time_in_force": time_in_force,
            "display_amount": display_amount,
            "post_only": post_only,
            "reject_post_only": reject_post_only,
            "reduce_only": reduce_only,
            "trigger_price": trigger_price,
            "trigger_offset": trigger_offset,
            "trigger": trigger,
            "advanced": advanced,
            "mmp": mmp,
            "valid_until": valid_until,
            "linked_order_type": linked_order_type,
            "trigger_fill_condition": trigger_fill_condition,
            "otoco_config": otoco_config,
            "isolated": isolated,
            "allocated_margin": allocated_margin,
        }
        return self._rpc("private/sell", params, models.PrivateBuyAndSellResponse)

    def private_set_leverage(
        self, instrument_name, leverage, *, subaccount_id=None, isolated=None
    ):
        """private/set_leverage"""
        params = {
            "instrument_name": instrument_name,
            "leverage": leverage,
            "subaccount_id": subaccount_id,
            "isolated": isolated,
        }
        return self._rpc(
            "private/set_leverage", params, models.PrivateSetLeverageResponse
        )

    def private_simulate_portfolio(
        self, currency, *, add_positions=None, simulated_positions=None
    ):
        """private/simulate_portfolio"""
        params = {
            "currency": currency,
            "add_positions": add_positions,
            "simulated_positions": simulated_positions,
        }
        return self._rpc(
            "private/simulate_portfolio",
            params,
            models.PrivateSimulatePortfolioResponse,
        )

    def private_submit_transfer_between_subaccounts(
        self, currency, amount, destination, *, source=None, nonce=None
    ):
        """private/submit_transfer_between_subaccounts"""
        params = {
            "currency": currency,
            "amount": amount,
            "destination": destination,
            "source": source,
            "nonce": nonce,
        }
        return self._rpc(
            "private/submit_transfer_between_subaccounts",
            params,
            models.PrivateSubmitTransferResponse,
        )

    def public_auth(self, grant_type, token):
        """public/auth"""
        params = {"grant_type": grant_type, "token": token}
        return self._rpc("public/auth", params, models.PublicAuthResponse)

    def public_get_announcements(self, *, start_timestamp=None, count=None):
        """public/get_announcements"""
        params = {"start_timestamp": start_timestamp, "count": count}
        return self._rpc(
            "public/get_announcements", params, models.PublicGetAnnouncementsResponse
        )

    def public_get_book_summary_by_currency(self, currency, *, kind=None):
        """public/get_book_summary_by_currency"""
        params = {"currency": currency, "kind": kind}
        return self._rpc(
            "public/get_book_summary_by_currency",
            params,
            models.PublicGetBookSummaryResponse,
        )

    def public_get_book_summary_by_instrument(self, instrument_name):
        """public/get_book_summary_by_instrument"""
        params = {"instrument_name": instrument_name}
        return self._rpc(
            "public/get_book_summary_by_instrument",
            params,
            models.PublicGetBookSummaryResponse,
        )

    def public_get_combo_details(self, combo_id):
        """public/get_combo_details"""
        params = {"combo_id": combo_id}
        return self._rpc(
            "public/get_combo_details", params, models.PublicGetComboDetailsResponse
        )

    def public_get_combo_ids(self, currency, *, state=None):
        """public/get_combo_ids"""
        params = {"currency": currency, "state": state}
        return self._rpc(
            "public/get_combo_ids", params, models.PublicGetComboIdsResponse
        )

    def public_get_combos(self, currency):
        """public/get_combos"""
        params = {"currency": currency}
        return self._rpc("public/get_combos", params, models.PublicGetCombosResponse)

    def public_get_contract_size(self, instrument_name):
        """public/get_contract_size"""
        params = {"instrument_name": instrument_name}
        return self._rpc(
            "public/get_contract_size", params, models.PublicGetContractSizeResponse
        )

    def public_get_currencies(self):
        """public/get_currencies"""
        params = {}
        return self._rpc(
            "public/get_currencies", params, models.PublicGetCurrenciesResponse
        )

    def public_get_delivery_prices(self, index_name, *, offset=None, count=None):
        """public/get_delivery_prices"""
        params = {"index_name": index_name, "offset": offset, "count": count}
        return self._rpc(
            "public/get_delivery_prices", params, models.PublicGetDeliveryPricesResponse
        )

    def public_get_expirations(self, currency, kind, *, currency_pair=None):
        """public/get_expirations"""
        params = {"currency": currency, "kind": kind, "currency_pair": currency_pair}
        return self._rpc(
            "public/get_expirations", params, models.PublicGetExpirationsResponse
        )

    def public_get_funding_chart_data(self, instrument_name, length):
        """public/get_funding_chart_data"""
        params = {"instrument_name": instrument_name, "length": length}
        return self._rpc(
            "public/get_funding_chart_data",
            params,
            models.PublicGetFundingChartDataResponse,
        )

    def public_get_funding_rate_history(
        self, instrument_name, start_timestamp, end_timestamp
    ):
        """public/get_funding_rate_history"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        }
        return self._rpc(
            "public/get_funding_rate_history",
            params,
            models.PublicGetFundingRateHistoryResponse,
        )

    def public_get_funding_rate_value(
        self, instrument_name, start_timestamp, end_timestamp
    ):
        """public/get_funding_rate_value"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        }
        return self._rpc(
            "public/get_funding_rate_value",
            params,
            models.PublicGetFundingRateValueResponse,
        )

    def public_get_historical_volatility(self, currency):
        """public/get_historical_volatility"""
        params = {"currency": currency}
        return self._rpc(
            "public/get_historical_volatility",
            params,
            models.PublicGetHistoricalVolatilityResponse,
        )

    def public_get_index_chart_data(self, index_name, range):
        """public/get_index_chart_data"""
        params = {"index_name": index_name, "range": range}
        return self._rpc(
            "public/get_index_chart_data",
            params,
            models.PublicGetIndexChartDataResponse,
        )

    def public_get_index_price(self, index_name):
        """public/get_index_price"""
        params = {"index_name": index_name}
        return self._rpc(
            "public/get_index_price", params, models.PublicGetIndexPriceResponse
        )

    def public_get_index_price_names(self, *, extended=None):
        """public/get_index_price_names"""
        params = {"extended": extended}
        return self._rpc(
            "public/get_index_price_names",
            params,
            models.PublicGetIndexPriceNamesResponse,
        )

    def public_get_instrument(self, instrument_name):
        """public/get_instrument"""
        params = {"instrument_name": instrument_name}
        return self._rpc(
            "public/get_instrument", params, models.PublicGetInstrumentResponse
        )

    def public_get_instruments(self, currency, *, kind=None, expired=None):
        """public/get_instruments"""
        params = {"currency": currency, "kind": kind, "expired": expired}
        return self._rpc(
            "public/get_instruments", params, models.PublicGetInstrumentsResponse
        )

    def public_get_last_settlements_by_currency(
        self,
        currency,
        *,
        type=None,
        count=None,
        continuation=None,
        search_start_timestamp=None
    ):
        """public/get_last_settlements_by_currency"""
        params = {
            "currency": currency,
            "type": type,
            "count": count,
            "continuation": continuation,
            "search_start_timestamp": search_start_timestamp,
        }
        return self._rpc(
            "public/get_last_settlements_by_currency",
            params,
            models.PublicSettlementResponse,
        )

    def public_get_last_settlements_by_instrument(
        self,
        instrument_name,
        *,
        type=None,
        count=None,
        continuation=None,
        search_start_timestamp=None
    ):
        """public/get_last_settlements_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "type": type,
            "count": count,
            "continuation": continuation,
            "search_start_timestamp": search_start_timestamp,
        }
        return self._rpc(
            "public/get_last_settlements_by_instrument",
            params,
            models.PublicSettlementResponse,
        )

    def public_get_last_trades_by_currency(
        self,
        currency,
        *,
        kind=None,
        start_id=None,
        end_id=None,
        start_timestamp=None,
        end_timestamp=None,
        count=None,
        sorting=None
    ):
        """public/get_last_trades_by_currency"""
        params = {
            "currency": currency,
            "kind": kind,
            "start_id": start_id,
            "end_id": end_id,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count": count,
            "sorting": sorting,
        }
        return self._rpc(
            "public/get_last_trades_by_currency",
            params,
            models.PublicTradesHistoryResponse,
        )

    def public_get_last_trades_by_currency_and_time(
        self,
        currency,
        start_timestamp,
        end_timestamp,
        *,
        kind=None,
        count=None,
        sorting=None
    ):
        """public/get_last_trades_by_currency_and_time"""
        params = {
            "currency": currency,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "kind": kind,
            "count": count,
            "sorting": sorting,
        }
        return self._rpc(
            "public/get_last_trades_by_currency_and_time",
            params,
            models.PublicTradesHistoryResponse,
        )

    def public_get_last_trades_by_instrument(
        self,
        instrument_name,
        *,
        start_seq=None,
        end_seq=None,
        start_timestamp=None,
        end_timestamp=None,
        count=None,
        sorting=None
    ):
        """public/get_last_trades_by_instrument"""
        params = {
            "instrument_name": instrument_name,
            "start_seq": start_seq,
            "end_seq": end_seq,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count": count,
            "sorting": sorting,
        }
        return self._rpc(
            "public/get_last_trades_by_instrument",
            params,
            models.PublicTradesHistoryResponse,
        )

    def public_get_last_trades_by_instrument_and_time(
        self,
        instrument_name,
        start_timestamp,
        end_timestamp,
        *,
        count=None,
        sorting=None
    ):
        """public/get_last_trades_by_instrument_and_time"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count": count,
            "sorting": sorting,
        }
        return self._rpc(
            "public/get_last_trades_by_instrument_and_time",
            params,
            models.PublicTradesHistoryResponse,
        )

    def public_get_mark_price_history(
        self, instrument_name, start_timestamp, end_timestamp
    ):
        """public/get_mark_price_history"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        }
        return self._rpc(
            "public/get_mark_price_history",
            params,
            models.PublicGetMarkPriceHistoryResponse,
        )

    def public_get_order_book(self, instrument_name, *, depth=None):
        """public/get_order_book"""
        params = {"instrument_name": instrument_name, "depth": depth}
        return self._rpc(
            "public/get_order_book", params, models.PublicGetOrderBookResponse
        )

    def public_get_order_book_by_instrument_id(self, instrument_id, *, depth=None):
        """public/get_order_book_by_instrument_id"""
        params = {"instrument_id": instrument_id, "depth": depth}
        return self._rpc(
            "public/get_order_book_by_instrument_id",
            params,
            models.PublicGetOrderBookResponse,
        )

    def public_get_supported_index_names(self, *, type=None):
        """public/get_supported_index_names"""
        params = {"type": type}
        return self._rpc(
            "public/get_supported_index_names",
            params,
            models.PublicGetIndexPriceNamesResponse,
        )

    def public_get_time(self):
        """public/get_time"""
        params = {}
        return self._rpc("public/get_time", params, models.PublicGetTimeResponse)

    def public_get_trade_volumes(self, *, extended=None):
        """public/get_trade_volumes"""
        params = {"extended": extended}
        return self._rpc(
            "public/get_trade_volumes", params, models.PublicGetTradesVolumesResponse
        )

    def public_get_volatility_index_data(
        self, currency, start_timestamp, end_timestamp, resolution
    ):
        """public/get_volatility_index_data"""
        params = {
            "currency": currency,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "resolution": resolution,
        }
        return self._rpc(
            "public/get_volatility_index_data",
            params,
            models.PublicGetVolatilityIndexDataResponse,
        )

    def public_status(self):
        """public/status"""
        params = {}
        return self._rpc("public/status", params, models.PublicStatusResponse)

    def public_test(self, *, expected_result=None):
        """public/test"""
        params = {"expected_result": expected_result}
        return self._rpc("public/test", params, models.PublicTestResponse)

    def public_ticker(self, instrument_name):
        """public/ticker"""
        params = {"instrument_name": instrument_name}
        return self._rpc("public/ticker", params, models.PublicTickerResponse)

    def public_tickers_by_currency(self, currency, *, kind=None, depth=None):
        """public/tickers_by_currency"""
        params = {"currency": currency, "kind": kind, "depth": depth}
        return self._rpc(
            "public/tickers_by_currency", params, models.PublicTickersByCurrencyResponse
        )


class GeneratedWSMixin:
    """RPC methods the gateway serves only over WebSocket. Mixed into
    DeribitRetailWSClient only."""

    def private_disable_cancel_on_disconnect(self, *, scope=None):
        """private/disable_cancel_on_disconnect"""
        params = {"scope": scope}
        return self._rpc(
            "private/disable_cancel_on_disconnect", params, models.OkResponse
        )

    def private_enable_cancel_on_disconnect(self, *, scope=None):
        """private/enable_cancel_on_disconnect"""
        params = {"scope": scope}
        return self._rpc(
            "private/enable_cancel_on_disconnect", params, models.OkResponse
        )

    def private_get_access_log(self, *, offset=None, count=None):
        """private/get_access_log"""
        params = {"offset": offset, "count": count}
        return self._rpc(
            "private/get_access_log", params, models.PrivateGetAccessLogResponse
        )

    def private_get_cancel_on_disconnect(self, *, scope=None):
        """private/get_cancel_on_disconnect"""
        params = {"scope": scope}
        return self._rpc(
            "private/get_cancel_on_disconnect",
            params,
            models.PrivateGetCancelOnDisconnectResponse,
        )

    def private_logout(self, *, invalidate_token=None):
        """private/logout"""
        params = {"invalidate_token": invalidate_token}
        return self._rpc("private/logout", params, None)

    def public_disable_heartbeat(self):
        """public/disable_heartbeat"""
        params = {}
        return self._rpc("public/disable_heartbeat", params, models.OkResponse)

    def public_get_tradingview_chart_data(
        self, instrument_name, start_timestamp, end_timestamp, resolution
    ):
        """public/get_tradingview_chart_data"""
        params = {
            "instrument_name": instrument_name,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "resolution": resolution,
        }
        return self._rpc(
            "public/get_tradingview_chart_data",
            params,
            models.PublicGetTradingviewChartDataResponse,
        )

    def public_hello(self, client_name, client_version):
        """public/hello"""
        params = {"client_name": client_name, "client_version": client_version}
        return self._rpc("public/hello", params, models.PublicTestResponse)

    def public_set_heartbeat(self, interval):
        """public/set_heartbeat"""
        params = {"interval": interval}
        return self._rpc("public/set_heartbeat", params, models.OkResponse)

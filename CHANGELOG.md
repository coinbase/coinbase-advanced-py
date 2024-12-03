# Changelog

## [1.8.2] - 2024-DEC-3

### Added
- More defined custom response type objects
- New fields for`Account`, `HistoricalMarketTrade` and `GetProductBookResponse`

### Changed
- Removed redundant response enum types 
- Removed redundant Public endpoint response types, now use same response types as Product endpoints
- Move custom object locations to their respective endpoints where response objects are defined

## [1.8.1] - 2024-NOV-15

### Added
- Support for converting custom REST and WebSocket response type objects to dict via new `to_dict()` function

### Fixed
- Importing from `coinbase.websocket.types`

## [1.8.0] - 2024-NOV-12

### Added
- Custom response type object for WebSocket channels

## [1.7.0] - 2024-OCT-16

### Added
- Custom response types to REST endpoints
- Dot-notation and auto-completing fields for defined objects

## [1.6.2] - 2024-SEP-09

### Added
- Support for RESTClient to append rate limit response headers to REST response bodies by setting `rate_limit_headers` to `True`.

## [1.6.1] - 2024-SEP-05

### Added
- Add WSUserClient to SDK documents

## [1.6.0] - 2024-SEP-05

### Added
- Support for WSUserClient to connect to the Coinbase Advanced Trade WebSocket user channel and futures_balance_summary channel

## [1.5.0] - 2024-AUG-21

### Added
- `get_all_products` parameter to `get_products` and `get_public_products`
- `aggregation_price_increment` parameter to `get_product_book` and `get_public_product_book`
- Support for API key permissions endpoint with`get_api_key_permissions`
- Support for auto generating unique client_order_id when set to empty string
- Support for Futures Balance Summary Channel in `WSClient`

### Changed
- Heartbeats channel methods no longer require `product_ids`

## [1.4.3] - 2024-JUL-22

### Added
- `order_ids`, `time_in_forces` and `sort_by` parameters in List Orders
- `trade_ids` and `sort_by` in List Fills

### Changed
- `skip_fcm_risk_check` parameter removed from various Orders methods.
- `product_id` and `order_type` has been replaced by `product_ids` and `order_types` in List Orders
- `order_id` and `product_id` has been replaced by `order_ids` and `product_ids` in List Fills

## [1.4.2] - 2024-JUN-17

### Added
- `retail_portfolio_id` to the `get_fills` method.
- `get_tradability_status` to the `get_product` and `get_products` method.

## [1.4.1] - 2024-MAY-24

### Changed
- `iss` on the signed JWT changed from `coinbase-cloud` to `cdp`

## [1.4.0] - 2024-MAY-21

### Added
- Support for market order buys in base currency with `base_size` in the `market_order_buy` and `preview_market_order_buy` methods
- Support for the following Futures Intraday Leverage API endpoints:
    - GetCurrentMarginWindow
    - GetIntradayMarginSetting 
    - SetIntradayMarginSetting
- Support for the following Perpetual Futures Trading API endpoints:
    - Get Perpetuals Portfolio Asset Balances
    - Opt-In Multi Asset Collateral

## [1.3.0] - 2024-MAY-6

### Added
- Support for limit Fill-or-Kill (FOK) order types
- Support for trigger bracket orders
- Support for public endpoints in RESTClient and public channels in WSClient that do not require authentication
- `retail_portfolio_id` to `get_accounts` method

### Changed
- "Coinbase Cloud" now referred to as "Coinbase Developer Platform (CDP)"

## [1.2.2] - 2024-APR-9

### Added
- Support for ClosePosition endpoint

### Changed
- Audience no longer included in JWT generation

## [1.2.1] - 2024-MAR-27

### Added
- `retail_portfolio_id` to all `preview_order` methods

### Changed
- Requests now made via request.Sessions() to reduce latency by reusing existing HTTP connection
- Timestamp no longer needed for websocket signing

## [1.2.0] - 2024-MAR-11

### Added
- Support for limit IOC order types
- Support for payments endpoints

### Changed
- get_unix_time() no longer requires authentication
- Log message when subscribing or unsubscribing via WSClient

### Fixed
- Unsubscribe_all() no longer sends message if not subscribed to any channel

## [1.1.3] - 2024-FEB-13

### Added
- Full MyPy annotations with return types for function definitions

## [1.1.2] - 2024-FEB-9

### Added
- Detailed documentation for all exposed functions of the SDK
- Support for PreviewOrder endpoint

## [1.1.1] - 2024-FEB-1

### Added
- Support for Perpetuals API endpoints

## [1.1.0] - 2024-JAN-31

### Added
- Initial release of WebSocket API client
- Verbose logging option for RESTClient

## [1.0.4] - 2024-JAN-29

### Fixed
- Fixed bug where `move_portfolio_funds` params were set incorrectly

## [1.0.3] - 2024-JAN-19

### Changed
- JWT generation expiry updated to 2 minutes to be consistent with Advanced Trade docs

## [1.0.2] - 2024-JAN-10

### Added
- Support for files for using JSON files for API key and secret
- Improve user facing messages for common errors

## [1.0.1] - 2024-JAN-3

### Added
- Support for Futures API endpoints

## [1.0.0] - 2023-DEC-18

### Added
- Initial release of the Coinbase Advanced Trading API Python SDK

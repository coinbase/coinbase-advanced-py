# Changelog

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

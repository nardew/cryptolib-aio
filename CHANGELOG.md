# Changelog

All notable changes to this project will be documented in this file.

The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Pending release]

## [3.10.0] - 2021-04-21

### Added

- `bitpanda` supports update of orders via streams (see `BitpandaWebsocket.py:UpdateOrderMessage`)

## [3.9.0] - 2021-03-14

### Added

- testnet endpoints added to `binance`, see `create_binance_testnet_client`
- different API clusters can now be selected in `binance`, see `binance.enums.APICluster`
- `get_best_orderbook_ticker` ticker added to `bitvavo`

## [3.8.1] - 2021-03-14

### Added

- following ticker calls added to the `bitvavo` client: `get_24h_price_ticker`, `get_price_ticker`.

## [3.8.0] - 2021-02-28

### Added

- `eterbase` exchange added

## [3.7.0] - 2021-01-15

### Added

- `bitpanda` REST API supports update of existing orders

## [3.6.1] - 2020-10-05

### Fixed

- `bitpanda` websocket order API supports missing `time_in_force` and `is_post_only` attributes

## [3.6.0] - 2020-09-15

### Added

- dead man's switch added into `bitpanda`

### Fixed

- support for python 3.6

## [3.5.0] - 2020-09-08

### Added

- new REST endpoints (mainly deposits and withdrawals) added into `bitpanda`
- an option to start websockets in a delayed mode (see `CryptoXLibClient.start_websockets(...)`). Useful when server does not support too many websocket connections opened at the same time
- support for `hitbtc`'s duplex websockets including order creation/cancellation

## [3.4.0] - 2020-09-01

### Added

- new `TRADING` subscription added into `bitpanda`
- new `ORDERS` subscription added into `bitpanda`
- additional `Time In Force` options added into `bitpanda`

## [3.3.0] - 2020-08-30

### Added

- `HitBTC` exchange added
-  `candlestick` websocket added into `binance`

## [3.2.1] - 2020-04-29

### Added

- `binance`'s `all market ticker` subscription added 

### Changed

- Fixed: `BTSE` websocket authorization complies with the new authorization handshake

## [3.2.0] - 2020-04-19

### Added

- `AAX` exchange added

### Changed

- `BTSE`'s `get_exchange_info` now supports mode to return info for all pairs and not just for the selected one
- Fixed: `BTSE` websockets are not losing connection when inactive

## [3.1.0] - 2020-04-10

### Added

- `BTSE` exchange added
- New unit tests for `bitpanda` and `bitforex`

### Changed

- Fixed: `bitvavo` callback invocation

## 3.0.0 - 2020-03-31

The official release of `cryptoxlib-aio`.

[Pending release]: https://github.com/nardew/cryptoxlib-aio/compare/3.10.0...HEAD
[3.10.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.9.0...3.10.0
[3.9.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.8.1...3.9.0
[3.8.1]: https://github.com/nardew/cryptoxlib-aio/compare/3.8.0...3.8.1
[3.8.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.7.0...3.8.0
[3.7.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.6.1...3.7.0
[3.6.1]: https://github.com/nardew/cryptoxlib-aio/compare/3.6.0...3.6.1
[3.6.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.5.0...3.6.0
[3.5.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.4.0...3.5.0
[3.4.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.3.0...3.4.0
[3.3.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.2.1...3.3.0
[3.2.1]: https://github.com/nardew/cryptoxlib-aio/compare/3.2.0...3.2.1
[3.2.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.1.0...3.2.0
[3.1.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.0.0...3.1.0

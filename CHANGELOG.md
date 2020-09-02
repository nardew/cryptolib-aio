# Changelog

All notable changes to this project will be documented in this file.

The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Pending release]

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

[Pending release]: https://github.com/nardew/cryptoxlib-aio/compare/3.4.0...HEAD
[3.4.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.3.0...3.4.0
[3.3.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.2.1...3.3.0
[3.2.1]: https://github.com/nardew/cryptoxlib-aio/compare/3.2.0...3.2.1
[3.2.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.1.0...3.2.0
[3.1.0]: https://github.com/nardew/cryptoxlib-aio/compare/3.0.0...3.1.0

import asyncio
import logging
import os

from cryptolib.CryptoLib import CryptoLib
from cryptolib.clients.liquid import enums
from cryptolib.Pair import Pair
from cryptolib.clients.liquid.LiquidWebsocket import OrderBookSideSubscription, OrderBookSubscription, OrderSubscription

LOG = logging.getLogger("cryptolib")
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())

print(f"Available loggers: {[name for name in logging.root.manager.loggerDict]}")


async def order_book_update(response : dict) -> None:
    print(f"Callback order_book_update: [{response}]")


async def order_book_update2(response : dict) -> None:
    print(f"Callback order_book_update2: [{response}]")


async def order_book_update3(response : dict) -> None:
    print(f"Callback order_book_update3: [{response}]")


async def order_update(response : dict) -> None:
    print(f"Callback order_update: [{response}]")


async def run():
    api_key = os.environ['LIQUIDAPIKEY']
    sec_key = os.environ['LIQUIDSECKEY']

    liquid = CryptoLib.create_liquid_client(api_key, sec_key)

    # Bundle several subscriptions into a single websocket
    liquid.compose_subscriptions([
        OrderBookSideSubscription(pair = Pair('BTC', 'USD'), order_side = enums.OrderSide.BUY, callbacks = [order_book_update]),
        #OrderBookSubscription(pair = Pair('ETH', 'USD'), callbacks = [order_book_update2]),
        #OrderBookSubscription(pair = Pair('XRP', 'USD'), callbacks = [order_book_update3]),
        #OrderSubscription(quote = "USD", callbacks = [order_update])
    ])

    # Execute all websockets asynchronously
    await liquid.start_websockets()

    await liquid.close()

if __name__ == "__main__":
    asyncio.run(run())

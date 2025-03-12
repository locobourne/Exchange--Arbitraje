from pybit.unified_trading import WebSocket
from time import sleep
ws = WebSocket(
    testnet=True,
    channel_type="spot",
)
def handle_message(message):
    print(message)
ws.trade_stream(
    symbol="BTCUSDT",
    callback=handle_message
)
while True:
    sleep(0.0001)
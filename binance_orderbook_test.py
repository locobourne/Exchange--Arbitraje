from websocket import WebSocketApp
import json

# Individual Symbol Book Ticker Streams
# Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol. Multiple <symbol>@bookTicker streams can be subscribed to over one connection.

# ej: dogeusdt@bookTicker

# Stream Name: <symbol>@bookTicker
# Update Speed: Real-time
#
# Payload:
# {
#   "u":400900217,     // order book updateId
#   "s":"BNBUSDT",     // symbol
#   "b":"25.35190000", // best bid price
#   "B":"31.21000000", // best bid qty
#   "a":"25.36520000", // best ask price
#   "A":"40.66000000"  // best ask qty
# }

def on_error(ws_binance, error):
    print(error)

def on_message(ws_binance, msg):
    tick = json.loads(msg)
    print('===================================================================================================================================================')
    print(f'El mejor precio de COMPRA para {tick["s"]} es de {tick["a"]}$ con una cantidad de {int(float(tick["A"]))} DOGE')
    print(f'El mejor precio de VENTA para {tick["s"]} es de {tick["b"]}$ con una cantidad de {int(float(tick["B"]))} DOGE')


def on_close(ws_binance, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws_binance):
    print("Opened connection")

binance_endpoint = 'wss://stream.binance.com:9443/ws/btcusdt@bookTicker'


ws_binance = WebSocketApp(binance_endpoint,
                          on_open=on_open,
                          on_message=on_message,
                          on_error=on_error,
                          on_close=on_close)

ws_binance.run_forever()
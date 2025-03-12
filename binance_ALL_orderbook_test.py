from websocket import WebSocketApp
import json
# Stream Description#
# Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.
# ej: 'wss://fstream.binance.com/ws/!bookTicker' // ALL COINS REALTIME
#
# Stream Name#: !bookTicker
# Update Speed#: Real-time
#
# Payload:
# {
#   "e":"bookTicker",         // event type
#   "u":400900217,            // order book updateId
#   "E": 1568014460893,   // event time
#   "T": 1568014460891,   // transaction time
#   "s":"BNBUSDT",            // symbol
#   "b":"25.35190000",        // best bid price
#   "B":"31.21000000",        // best bid qty
#   "a":"25.36520000",        // best ask price
#   "A":"40.66000000"         // best ask qty
# }
def on_error(ws_binance, error):
    print(error)

def on_message(ws_binance, msg):
    tick = json.loads(msg)
    print('===================================================================================================================================================')
    print(f'El mejor precio de COMPRA para {tick["s"]} es de {tick["a"]}$ con una cantidad de {int(float(tick["A"]))} monedas')
    print(f'El mejor precio de VENTA para {tick["s"]} es de {tick["b"]}$ con una cantidad de {int(float(tick["B"]))} monedas')


def on_close(ws_binance, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws_binance):
    print("Opened connection")

binance_endpoint = 'wss://fstream.binance.com/ws/!bookTicker'


ws_binance = WebSocketApp(binance_endpoint,
                          on_open=on_open,
                          on_message=on_message,
                          on_error=on_error,
                          on_close=on_close)

ws_binance.run_forever()
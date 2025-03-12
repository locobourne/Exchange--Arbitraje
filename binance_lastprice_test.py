from websocket import WebSocketApp
import json
import datetime
# Aggregate Trade Streams
# The Aggregate Trade Streams push trade information that is aggregated for a single taker order.
# Trades de una hora especifica
# Stream Name: <symbol>@aggTrade
#
# Todos los trades de una hora especifica
# Stream Name: <symbol>@trade
#
#
# Update Speed: Real-time
#
# Payload:
# {
#   "e": "aggTrade",    // Event type
#   "E": 1672515782136, // Event time
#   "s": "BNBBTC",      // Symbol
#   "a": 12345,         // Aggregate trade ID
#   "p": "0.001",       // Price
#   "q": "100",         // Quantity
#   "f": 100,           // First trade ID
#   "l": 105,           // Last trade ID
#   "T": 1672515782136, // Trade time
#   "m": true,          // Is the buyer the market maker?
#   "M": true           // Ignore
# }

def on_error(ws_binance, error):
    print(error)

def on_message(ws_binance, msg):
    tick = json.loads(msg)
    your_dt = datetime.datetime.fromtimestamp(int(tick['T']) / 1000)
    #print(your_dt.strftime("%Y-%m-%d %H:%M:%S"))
    print('===================================================================================================================================================')
    print(f'La ultima venta de {tick["s"]} fue de {tick["p"]}$ y de una cantidad de {float(tick["q"])} DOGE a las {your_dt.strftime("%H:%M:%S")}')



def on_close(ws_binance, close_status_code, close_msg):
    print("### Closed ###")

def on_open(ws_binance):
    print("### Opened connection ###")

binance_endpoint = 'wss://stream.binance.com:9443/ws/btcusdt@aggTrade'


ws_binance = WebSocketApp(binance_endpoint,
                          on_open=on_open,
                          on_message=on_message,
                          on_error=on_error,
                          on_close=on_close)

ws_binance.run_forever()
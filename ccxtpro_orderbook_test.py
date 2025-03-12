import ccxt.pro as ccxtpro
from asyncio import run
import datetime

print('CCXT version', ccxtpro.__version__)
print('Supported exchanges:', ccxtpro.exchanges)

# exchange = ccxtpro.binance({'newUpdates': False})
# print(exchange.options)

async def main():
    exchange = ccxtpro.bitget({'newUpdates': True})
    while True:
        #orderbook = await exchange.watch_order_book('DOGE/USDT')
        #print(orderbook['asks'][0], orderbook['bids'][0])
        ticker = await exchange.watch_ticker(['DOGE/USDT', 'BTC/USDT'])
        #print(exchange.iso8601(exchange.milliseconds()), ticker)
        print(ticker)
        your_dt = datetime.datetime.fromtimestamp(int(ticker['timestamp']) / 1000)
        if ticker["askVolume"] == None:
            ask_volume = 'NO_INFO'
        else:
            ask_volume = int(float(ticker["askVolume"]))

        if ticker["bidVolume"] == None:
            bid_volume = 'NO_INFO'
        else:
            bid_volume = int(float(ticker["bidVolume"]))

        print('===================================================================================================================================================')
        print(f'El mejor precio de COMPRA para {ticker["symbol"]} es de {ticker["ask"]}$ con una cantidad de {ask_volume} monedas')
        print(f'El mejor precio de VENTA para {ticker["symbol"]} es de {ticker["bid"]}$ con una cantidad de {bid_volume} monedas')
        #print(f'La ultima venta de {ticker["symbol"]} fue de {ticker["close"]}$ y de una cantidad de {float(ticker["info"]["Q"])} DOGE a las {your_dt.strftime("%H:%M:%S")}')  //BINANCE
        print(f'La ultima venta de {ticker["symbol"]} fue de {ticker["close"]}$ y de una cantidad de {float(ticker["baseVolume"])} DOGE a las {your_dt.strftime("%H:%M:%S")}')
    await exchange.close()



run(main())
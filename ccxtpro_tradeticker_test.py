import ccxt.pro as ccxtpro
from asyncio import run
import datetime


print('CCXT version', ccxtpro.__version__)

list = ['DOGE/USDT', 'BTC/USDT']

async def main():
    exchange = ccxtpro.binance({'newUpdates': True})
    while True:
        ticker = await exchange.watch_trades_for_symbols(list)
        your_dt = datetime.datetime.fromtimestamp(int(ticker[0]['timestamp']) / 1000)
        #if ticker[0]['symbol'] == 'DOGE/USDT':
        print('===================================================================================================================================================')
        print(f'La ultima venta de {ticker[0]["symbol"]} fue de {ticker[0]["price"]}$ y de una cantidad de {float(ticker[0]["amount"])} DOGE a las {your_dt.strftime("%H:%M:%S")}')
    await exchange.close()


run(main())
import ccxt
import pandas as pd
from time import sleep



binance = ccxt.binance()
market_binance = binance.fetchOrderBook('DOGEUSDT',2)
#df = pd.DataFrame(market_binance)

#print(df)
print(market_binance)
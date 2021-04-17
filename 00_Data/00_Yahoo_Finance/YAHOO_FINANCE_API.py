import yfinance as yf
import pandas as pd
from yfinance import Ticker
import os

os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')
tickers = pd.read_csv('most_common.csv', sep='|', lineterminator='\n')
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/00_Yahoo_Finance')
tickerStrings = tickers.loc[0:250, 'ticker']

# tickerStrings = ['AMC', 'GME', 'BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','TSLA',
# 'FORD','ASO','MVIS','AMD','GM','WIRE','M','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']


df_list = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", start="2019-07-01")
    data['Stock'] = ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

# save to csv
df.to_csv('Yahoo_Finance_DataV2.csv')























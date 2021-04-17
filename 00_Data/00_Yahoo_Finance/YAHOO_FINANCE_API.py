import yfinance as yf
import pandas as pd
import datetime as dt
from yfinance import Ticker
import os

os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')
tickers = pd.read_csv('most_common.csv', sep='|', lineterminator='\n')
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/00_Yahoo_Finance')
tickerStrings = tickers.loc[0:250, 'ticker']

# tickerStrings = ['AMC', 'GME', 'BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','TSLA',
# 'FORD','ASO','MVIS','AMD','GM','WIRE','M','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']

stock_data = pd.DataFrame(columns=['date', 'ticker', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])


for ticker in tickerStrings:
    dates = pd.date_range(start='2019-07-01', end='2021-04-17', freq='D')
    df = pd.DataFrame(dates, columns=['date'])
    df.date = pd.to_datetime(df.date).dt.date
    df['ticker'] = ticker
    ydata = yf.download(ticker, group_by="Ticker", start="2019-07-01")
    ydata['date'] = pd.to_datetime(ydata.index).date

    merged = pd.merge(df, ydata, left_on='date', right_on='date', how='left')
    stock_data.append(merged)

# combine all dataframes into a single dataframe
# df = pd.concat(df_list)

# save to csv
stock_data.to_csv('Yahoo_Finance_Data.csv')























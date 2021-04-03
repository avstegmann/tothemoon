
import yfinance as yf
import pandas as pd
from yfinance import Ticker

# get stock info

AMC_Entertainment_Holdings = yf.Ticker('AMC')
Gamestop = yf.Ticker('GME')
BlackBerry_Limited = yf.Ticker('BB')
Koss_Corporation = yf.Ticker('KOSS')
Express = yf.Ticker('EXPR')


hist_AMC_Entertainment_Holdings = AMC_Entertainment_Holdings.history(period="max")


print(hist_AMC_Entertainment_Holdings)

print('test_für_geileren Code')

tickerStrings = ['AAPL', 'MSFT']
df_list = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='2d')
    data['ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

# save to csv
df.to_csv('ticker.csv')
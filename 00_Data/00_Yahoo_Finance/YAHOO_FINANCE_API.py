
import yfinance as yf
import pandas as pd
from yfinance import Ticker


tickerStrings = ['AMC', 'GME', 'BB']
df_list = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='max')
    data['Stock'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

# save to csv
df.to_csv('Yahoo_Finance_Data.csv')
import yfinance as yf
import pandas as pd
import os

# get the 250 most common stock tickers from the data set
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')
tickers = pd.read_csv('most_common.csv', sep='|', lineterminator='\n')
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/00_Yahoo_Finance')
tickerStrings = tickers.loc[0:250, 'ticker']

# create DataFrame to store stock data
stock_data = pd.DataFrame(columns=['date', 'ticker', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])


for ticker in tickerStrings:
    # set full date range that includes weekends
    dates = pd.date_range(start='2019-07-01', end='2021-04-17', freq='D')
    df = pd.DataFrame(dates, columns=['date'])
    # drop minutes from the dates
    df.date = pd.to_datetime(df.date).dt.date
    # add ticker to provide key for data aggregation in tableau
    df['ticker'] = ticker
    # get data from yahoo
    ydata = yf.download(ticker, group_by="Ticker", start="2019-07-01")
    ydata['date'] = pd.to_datetime(ydata.index).date

    # merge data to stock data Dataframe
    merged = pd.merge(df, ydata, left_on='date', right_on='date', how='left')
    stock_data = stock_data.append(merged)

# save to csv
stock_data.to_csv('Yahoo_Finance_Data.csv')























import yfinance as yf
import pandas as pd
import tqdm  # https://pypi.org/project/tqdm/
import os

# load the list of the 1000 most common tickers on WSB in our data set
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/02_Reddit')
tickers = pd.read_csv('most_common.csv', sep='|', lineterminator='\n')
tickers = pd.DataFrame(tickers.loc[0:999])
tickers['market_cap'] = ''

'''
iterate through each ticker and load the corresponding market capitalization 
(this will take a considerable amount of time)
'''
with tqdm.tqdm(total=tickers.__len__()) as pbar:
    for ticker in tickers.iterrows():
        stock = yf.Ticker(ticker[1].ticker)
        try:
            tickers.loc[ticker[0], 'market_cap'] = stock.info['marketCap']
        except KeyError:
            tickers.loc[ticker[0], 'market_cap'] = 0
        pbar.update(1)

tickers.to_csv('most_common_cap.csv')



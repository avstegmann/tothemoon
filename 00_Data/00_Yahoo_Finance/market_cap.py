import yfinance as yf
import pandas as pd
import tqdm
import os

os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')
tickers = pd.read_csv('most_common.csv', sep='|', lineterminator='\n')
tickers = pd.DataFrame(tickers.loc[0:999])
tickers['market_cap'] = ''

with tqdm.tqdm(total=tickers.__len__()) as pbar:
    for ticker in tickers.iterrows():
        stock = yf.Ticker(ticker[1].ticker)
        try:
            tickers.loc[ticker[0], 'market_cap'] = stock.info['marketCap']
        except KeyError:
            tickers.loc[ticker[0], 'market_cap'] = 0
        pbar.update(1)

tickers.to_csv('most_common_cap.csv')



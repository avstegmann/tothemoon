import pandas as pd
import re
from string import punctuation
import os
import tqdm

os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit/archive')
df = pd.read_csv('full_no-dupes.csv', sep='|', lineterminator='\n')
df = df.dropna(subset=['selftext'])
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')
# https://stockanalysis.com/stocks/
ticker_names = pd.read_csv('ticker_name.csv', sep='|')

PUNCTUATION = set(punctuation)
BLACKLIST = ['all', 'and', 'are', 'ath', 'atm', 'big', 'can', 'cdc', 'ceo', 'cfo', 'cnbc', 'cnn', 'company', 'covid',
             'cost', 'dfv', 'dow', 'eod', 'eow', 'eps', 'etf', 'faq', 'fda', 'fed', 'finra', 'fomo', 'for', 'fud',
             'fang', 'fyi', 'get', 'gdp', 'good', 'hodl', 'huge', 'home', 'imo', 'itm', 'leaps', 'low', 'mso', 'msr',
             'now', 'nyse', 'next', 'one', 'opec', 'otcbb', 'otm', 'out', 'ppp', 'real', 'see', 'sec', 'spac', 'tba',
             'the', 'tldr', 'usd', 'wsb', 'wsj', 'wtf', 'usb']


def tickerize(text):
    text = re.sub(r'[$]ROPE', '', text)
    caps = []
    for token in text.split():
        for p in PUNCTUATION:
            token = token.replace(p, '')
        if token.isupper() and len(token) > 2 and token.lower() not in BLACKLIST:
            caps.append(token)
    return caps.__str__()


def main():
    df['caps1'] = df.selftext.apply(lambda x: tickerize(x))
    df['caps2'] = df.title.apply(lambda x: tickerize(x))
    print('tickerized')
    df['list'] = ''

    with tqdm.tqdm(total=ticker_names.__len__()) as pbar:
        for _, ticker in ticker_names.iterrows():
            try:
                mask = df.caps1.str.contains(rf'\b{ticker.ticker}\b', regex=True)
                df.loc[mask, 'list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.ticker)
            try:
                mask = df.selftext.str.contains(ticker.comp_name)
                df.loc[mask, 'list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.comp_name)
            try:
                mask = df.caps2.str.contains(rf'\b{ticker.ticker}\b', regex=True)
                df.loc[mask, 'list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.ticker)
            try:
                mask = df.title.str.contains(ticker.comp_name)
                df.loc[mask, 'list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.comp_name)
            pbar.update(1)

    # https://stackoverflow.com/questions/479897/how-to-remove-duplicates-from-python-list-and-keep-order
    df.list = df.list.apply(lambda x: sorted(set(list(x.split()))))

    df.to_csv('reddit_posts.csv', sep='|', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()

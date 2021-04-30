from string import punctuation
import pandas as pd
import tqdm
import os
import re

# Source for the ticker symbols https://stockanalysis.com/stocks/

# load list of ticker and company names
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/02_Reddit')
ticker_names = pd.read_csv('ticker_name.csv', sep='|')

# load reddit posts
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/02_Reddit')
df = pd.read_csv('reddit_posts.csv', sep='|', lineterminator='\n')

PUNCTUATION = set(punctuation)
BLACKLIST = ['all', 'and', 'are', 'ath', 'atm', 'big', 'can', 'cdc', 'ceo', 'cfo', 'cnbc', 'cnn', 'company', 'covid',
             'cost', 'dfv', 'dow', 'eod', 'eow', 'eps', 'etf', 'faq', 'fda', 'fed', 'finra', 'fomo', 'for', 'fud',
             'fang', 'fyi', 'get', 'gdp', 'good', 'hodl', 'huge', 'home', 'imo', 'itm', 'leaps', 'low', 'mso', 'msr',
             'now', 'nyse', 'next', 'one', 'opec', 'otcbb', 'otm', 'out', 'ppp', 'real', 'see', 'sec', 'spac', 'tba',
             'the', 'tldr', 'usd', 'wsb', 'wsj', 'wtf', 'usb']


def tickerize(text):
    """
    This function splits a text into all upper case words that are longer than 2 characters and do not appear in the
    blacklist
    :param text: text
    :return: list
    """
    # delete all mentions of $ROPE as this is financial lingo for being invested and not a valid ticker
    text = re.sub(r'[$]ROPE', '', text)
    caps = []
    for token in text.split():
        # delete all punctuation
        for p in PUNCTUATION:
            token = token.replace(p, '')
        # append ticker to list if it meets the criteria
        if token.isupper() and len(token) > 2 and token.lower() not in BLACKLIST:
            caps.append(token)
    return caps.__str__()


def main():
    # create two lists of possible tickers, one from selftexts and one from titles
    df['caps1'] = df.selftext.apply(lambda x: tickerize(x))
    df['caps2'] = df.title.apply(lambda x: tickerize(x))
    print('tickerized')
    df['ticker_list'] = ''

    # iterate through all tickers and all company names and compare them to the ticker list or full texts
    with tqdm.tqdm(total=ticker_names.__len__()) as pbar:
        for _, ticker in ticker_names.iterrows():
            try:
                mask = df.caps1.str.contains(rf'\b{ticker.ticker}\b', regex=True)
                df.loc[mask, 'ticker_list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.ticker)
            try:
                mask = df.selftext.str.contains(ticker.comp_name)
                df.loc[mask, 'ticker_list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.comp_name)
            try:
                mask = df.caps2.str.contains(rf'\b{ticker.ticker}\b', regex=True)
                df.loc[mask, 'ticker_list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.ticker)
            try:
                mask = df.title.str.contains(ticker.comp_name)
                df.loc[mask, 'ticker_list'] += ticker.ticker + ' '
            except AttributeError:
                print('Attribute Error')
                print(ticker.comp_name)
            pbar.update(1)

    # https://stackoverflow.com/questions/479897/how-to-remove-duplicates-from-python-list-and-keep-order
    df.ticker_list = df.ticker_list.apply(lambda x: sorted(set(list(x.split()))))
    # df.to_csv('reddit_posts_safety.csv', sep='|', index=False, encoding='utf-8')
    output = df.drop(['caps1', 'caps2'], axis=1)
    output.to_csv('reddit_posts_incl_ticker.csv', sep='|', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()

from collections import Counter
import pandas as pd
import os
import ast
import tqdm

os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')

df = pd.read_csv('reddit_posts.csv', sep='|', lineterminator='\n')
df = df.drop_duplicates(subset='selftext')
df2 = pd.DataFrame(columns=['created_utc', 'id', 'ticker'])


# 25 categories of interest
out = df[['created_utc',
          'date',
          'ticker',
          'author',
          'author_fullname'
          'author_flair_text',
          'link_flair_text',
          'url',
          'title',
          'selftext',
          'num_comments',
          'num_crossposts',
          'score',
          'upvote_ratio',
          'id',
          'is_crosspostable',
          'is_meta',
          'is_self',
          'is_video',
          'no_follow',
          'allow_live_comments'
          'all_awardings',
          'total_awards_received',
          'awarders',
          'gildings']]



tickers = df.ticker_list.to_list()
ticker_list = []
for ticker in tickers:
    ticker_list.append(ast.literal_eval(ticker))

all_tickers = list(set([ticker for sublist in ticker_list for ticker in sublist]))
all_tickers.sort()

with tqdm.tqdm(total=len(all_tickers)) as pbar:
    for ticker in all_tickers:
        mask = df.ticker_list.str.contains(rf'\b{ticker}\b', regex=True)
        container = df2.append(df.loc[mask, ['created_utc', 'id']])
        container['ticker'] = ticker
        df2 = df2.append(container)
        pbar.update(1)


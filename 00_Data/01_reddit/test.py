from sentiment import get_sentiment
import os
import pandas as pd
from tqdm import tqdm


def main():
    print('df loaded')
    os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit/')
    df = pd.read_csv('reddit_posts.csv', sep='|', lineterminator='\n')

    df['sent'] = ''

    tqdm.pandas()

    df.sent = df.selftext.progress_apply(lambda txt: get_sentiment(txt))

    df.to_csv('reddit_posts_sent.csv', sep='|', encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
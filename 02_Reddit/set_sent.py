from sentiment import get_sentiment2  # import either get_sentiment1 or get_sentiment2
import os
import pandas as pd
from tqdm import tqdm


def main():
    os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/02_Reddit')
    df = pd.read_csv('reddit_posts_final.csv', sep='|', lineterminator='\n')
    print('df loaded')

    df['sent'] = ''

    tqdm.pandas()

    low = 0
    high = 4999
    end = len(df)

    while high < end:
        print(f'Batch to {high}')
        df.loc[low:high, 'sent'] = df.loc[low:high, 'selftext'].progress_apply(lambda txt: get_sentiment2(txt))
        df.to_csv('sent_test.csv', sep='|', encoding='utf-8', index=False)
        low = high + 1
        high += 5000
        if high > (end - low):
            print(f'Batch to {high}')
            df.loc[low:high, 'sent'] = df.loc[low:high, 'selftext'].progress_apply(lambda txt: get_sentiment2(txt))
            df.to_csv('sent_test.csv', sep='|', encoding='utf-8', index=False)
            break


if __name__ == '__main__':
    main()

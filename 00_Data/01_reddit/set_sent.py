from sentiment import get_sentiment
import os
import pandas as pd
from tqdm import tqdm


def main():
    print('df loaded')
    os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit/archive')
    df = pd.read_csv('second_aprilV2.csv', sep='|', lineterminator='\n')

    df['sent'] = ''

    tqdm.pandas()

    low = 0
    high = 2205
    end = 2206

    while high < end:
        print(f'Batch to {high}')
        df.loc[low:high, 'sent'] = df.loc[low:high, 'selftext'].progress_apply(lambda txt: get_sentiment(txt))
        df.to_csv('second_aprilV3.csv', sep='|', encoding='utf-8', index=False)
        low = high + 1
        high += 5000
        if high == end - 1:
            print(f'Batch to {high}')
            df.loc[low:high, 'sent'] = df.loc[low:high, 'selftext'].progress_apply(lambda txt: get_sentiment(txt))
            df.to_csv('second_aprilV3.csv', sep='|', encoding='utf-8', index=False)
            break


if __name__ == '__main__':
    main()

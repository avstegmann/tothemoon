import datetime as dt
import pandas as pd
import requests


def get_posts(data_type, after=None, before=None, ticker=None, **kwargs):
    """
    https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
    :param data_type: str, either: 'comment' or 'submission
    :param after:
    :param before:
    :param ticker
    :param kwargs: other arguments that are interpreted as payload
    :return:
    """
    print(ticker)
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    if after is None and before is None:
        print(kwargs)
        payload = kwargs
        request = requests.get(base_url, params=payload)
        data = request.json()
        df = pd.DataFrame.from_dict(data['data'])
    else:
        kwargs['before'] = before
        print(kwargs)
        payload = kwargs
        request = requests.get(base_url, params=payload)
        data = request.json()
        df = pd.DataFrame.from_dict(data['data'])
        kwargs['before'] = df.iloc[-1].created_utc
        date = kwargs['before']
        mes = df.__len__()
        print(mes)
        while date > after:
            payload = kwargs
            request = requests.get(base_url, params=payload)
            try:
                data = request.json()
                dump = pd.DataFrame.from_dict(data['data'])
                df = df.append(dump, ignore_index=True)
                kwargs['before'] = df.iloc[-1].created_utc
                date = kwargs['before']
                mes += (df.__len__() - mes)
                print('Status: ' + str(mes))
                if (mes % 5000) == 0:
                    df = df.replace("\n", " ", regex=True)
                    # https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
                    df.created_utc = pd.to_datetime(df.created_utc, unit='s')
                    df['date'] = pd.to_datetime(df.created_utc, unit='s').dt.date
                    df.to_csv('bucket.csv', mode='a', sep='|', index=False, encoding='utf-8', header=False)
                    df = pd.DataFrame(columns=['created_utc', 'full_link', 'selftext'])
                    mes = 100
                if (mes % 100) > 0:
                    break
            except:
                print('Error')
                pass
    df = df.replace("\n", " ", regex=True)
    # https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
    df.created_utc = pd.to_datetime(df.created_utc, unit='s')
    df['date'] = pd.to_datetime(df.created_utc, unit='s').dt.date
    df.to_csv('bucket.csv', mode='a', sep='|', index=False, encoding='utf-8', header=False)
    # if ticker is not None:
    #    df['ticker'] = ticker
    print('Total posts: ' + str(len(df)))
    # return df


def main():
    after = int(dt.datetime(2019, 6, 30).timestamp())
    before = int(dt.datetime(2019, 8, 8).timestamp())
    # df =
    get_posts('submission',
              subreddit='wallstreetbets',
              is_self=True,
              # selftext='RLX',  # For company names longer than 1 word use " "
              after=after,
              before=before,
              # ticker='RLX',
              fields=['created_utc', 'full_link', 'selftext'],
              size=100)
    #df.to_csv('all_posts_21.csv', sep='|', index=False, encoding='utf-8')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

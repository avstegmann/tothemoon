import datetime as dt
import pandas as pd
import requests


def get_posts(data_type, after=None, before=None, ticker=None, **kwargs):
    """
    https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
    :param data_type: str, either: 'comment' or 'submission
    :param after:
    :param before:
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
            data = request.json()
            dump = pd.DataFrame.from_dict(data['data'])
            df = df.append(dump, ignore_index=True)
            kwargs['before'] = df.iloc[-1].created_utc
            date = kwargs['before']
            mes += (df.__len__() - mes)
            print(mes)
            if (mes % 100) > 0:
                break
    df = df.replace("\n", " ", regex=True)
    # https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
    df.created_utc = pd.to_datetime(df.created_utc, unit='s')
    df['date'] = pd.to_datetime(df.created_utc, unit='s').dt.date
    df['ticker'] = ticker
    print('Total posts: ' + str(len(df)))
    return df


def main():
    after = int(dt.datetime(2019, 6, 30).timestamp())
    before = int(dt.datetime(2021, 4, 1).timestamp())
    df = get_posts('submission',
                   subreddit='wallstreetbets',
                   is_self=True,
                   selftext='RLX',  # For company names longer than 1 word use " "
                   after=after,
                   before=before,
                   ticker='RLX',
                   size=1000)
    df.to_csv('RLX.csv', sep='|', index=False, encoding='utf-8')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

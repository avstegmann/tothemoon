import datetime as dt
import pandas as pd
import json
import requests
from pandas import DataFrame


def get_posts(data_type, after=None, before=None, **kwargs):
    """
    https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
    :param data_type: str, either: 'comment' or 'submission
    :param after:
    :param before:
    :param kwargs: other arguments that are interpreted as payload
    :return:
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    if after is None and before is None:
        payload = kwargs
        request = requests.get(base_url, params=payload)
        data = request.json()
        return pd.DataFrame.from_dict(data['data'])
    else:
        kwargs['before'] = before
        date = before
        payload = kwargs
        request = requests.get(base_url, params=payload)
        data = request.json()
        df = pd.DataFrame.from_dict(data['data'])
        mes = df.__len__()
        print(mes)
        if mes == 1000:
            while date > after:
                payload = kwargs
                request = requests.get(base_url, params=payload)
                data = request.json()
                dump = pd.DataFrame.from_dict(data['data'])
                df = df.append(dump, ignore_index=True)
                kwargs['before'] = df.iloc[-1].created_utc
                date = kwargs['before']
                mes += 1000
                print(mes)
        df = df.replace("\n", " ", regex=True)
        df.created_utc = pd.to_datetime(df.created_utc, unit='s')
        return df


def main():
    after = int(dt.datetime(2020, 6, 1).timestamp())
    before = int(dt.datetime(2020, 9, 1).timestamp())
    df = get_posts('submission',
                   subreddit='wallstreetbets', is_self=True, selftext='GME', after=after, before=before, size=1000)
    df.to_csv('GME2.csv', sep='|', index=False, encoding='utf-8')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

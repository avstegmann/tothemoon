import datetime as dt
import pandas as pd
import requests


def get_posts(data_type, after=None, before=None, **kwargs):
    """
    https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
    :param data_type: str, either: 'comment' or 'submission'
    :param after: timestamp
    :param before: timestamp
    :param kwargs: other arguments that are interpreted as payload
    :return:
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    # kwargs['before'] = before
    print(kwargs)

    payload = kwargs
    request = requests.get(base_url, params=payload)
    data = request.json()
    df = pd.DataFrame(columns=kwargs['fields'])
    df = df.append(pd.DataFrame.from_dict(data['data']))

    # set before value to get the previous batch of 100 results
    kwargs['before'] = df.iloc[-1].created_utc
    date = kwargs['before']
    status = df.__len__()
    print(status)

    # delete line brakes to clean csv
    df = df.replace("\n", " ", regex=True)
    # first save -> normal mode
    df.to_csv('full.csv', sep='|', index=False, encoding='utf-8')
    # re-initialize DataFrame
    df = pd.DataFrame(columns=kwargs['fields'])

    # loop that runs until the 'after'-date is reached
    while date > after:
        payload = kwargs
        request = requests.get(base_url, params=payload)
        try:
            # same procedure as before
            data = request.json()
            dump = pd.DataFrame.from_dict(data['data'])
            df = df.append(dump, ignore_index=True)

            kwargs['before'] = df.iloc[-1].created_utc
            date = kwargs['before']
            status += (df.__len__() - status)
            print('Status: ' + str(status))

            # after 5000 results, save to file -> mode append
            if (status % 5000) == 0:
                df = df.replace("\n", " ", regex=True)
                df.to_csv('full.csv', mode='a', sep='|', index=False, encoding='utf-8', header=False)
                df = pd.DataFrame(columns=kwargs['fields'])
                status = 100
            if (status % 100) > 0:
                break
        except:
            print('Error')
            pass

    df = df.replace("\n", " ", regex=True)
    df.to_csv('full.csv', mode='a', sep='|', index=False, encoding='utf-8', header=False)
    df = pd.read_csv('full.csv', sep='|', lineterminator='\n')

    # convert date format https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
    df.created_utc = pd.to_datetime(df.created_utc, unit='s')
    df['date'] = pd.to_datetime(df.created_utc, unit='s').dt.date
    # safe to file -> mode write
    df.to_csv('full.csv', mode='w', sep='|', index=False, encoding='utf-8')
    print('Done')


def main():
    after = int(dt.datetime(2021, 4, 9).timestamp())
    # before = int(dt.datetime(2021, 4, 10, 19, 26, 00).timestamp())
    get_posts('submission',
              subreddit='wallstreetbets',
              is_self=True,
              after=after,
              # before=before,
              fields=['created_utc',
                      'author',
                      'author_fullname',
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
                      'allow_live_comments',
                      'all_awardings',
                      'total_awards_received',
                      'awarders',
                      'gildings'],
              size=100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

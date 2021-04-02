import pandas as pd
import json
import requests


def get_posts(data_type, **kwargs):
    """
    https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
    :param data_type: str, either: 'comment' or 'submission
    :param kwargs: other arguments that are interpreted as payload
    :return:
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)

    return request.json()


def main():
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

import pandas as pd

df = pd.read_csv('submissions_reddit.csv', sep=',')
df = df.replace("\n", " ", regex=True)
df.to_csv('submissions_reddit.csv', sep='|', encoding='utf-8', index=False)


# ------------------  02.04.20 Backup Code Reddit API ------------------

# pip install psaw
# pip install praw

import praw
from psaw import PushshiftAPI
import datetime as dt
import pandas as pd




r = praw.Reddit(
    client_id="RFV4JD4o7WaMmg",
    client_secret="ONq60_EDhK-FFUY80taWKxnzdBNcZQ",
    password="5Yfu>g86VVMK]ma?mb&X",
    user_agent="wsb_bot",
    username="unisg_wsb_bot",
)

api = PushshiftAPI(r)

start_epoch = int(dt.datetime(2020, 9, 1).timestamp())

list(api.search_submissions(after=start_epoch,
                            q='GME',
                            subreddit='wallstreetbets',
                            filter=['url', 'author', 'title', 'subreddit'],
                            limit=10))

df = pd.Dataframe([thing.d_ for thing in gen])


import datetime as dt
import pandas as pd
import requests

data_type = 'submission' # oder comment
after = int(dt.datetime(2021, 4, 9).timestamp())

base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
payload = {
    'subreddit': 'wallstreetbets',
    'is_self': True, # filtert nach submissions, die nur Text enthalten
    'fields': ['created_utc',
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
               'gildings'], # die 25 relevanten Felder für unsere Analyse
    'size': 100
}

request = requests.get(base_url, params=payload) # Anfrage an die API senden
data = request.json() # JSON auslesen
df = pd.DataFrame(columns=payload['fields']) # DataFrame mit den gewünschten Feldern als Spalten
df = df.append(pd.DataFrame.from_dict(data['data']))
df = df.replace("\n", " ", regex=True)
df.to_csv('full.csv', sep='|', index=False, encoding='utf-8') # Zwischenspeichern zur Datensicherung

# Mit den folgenden beiden Schritten, kann Schrittweise "in der Zeit zurückgegangen werden, indem man das Datum des
# ältesten Posts als neuen 'before' Parameter an folgende Anfragen anfügt.
payload['before'] = df.iloc[-1].created_utc
date = payload['before']

# Den oben beschriebenen Prozess haben wir dann in einer While-Schleife, bis zum 'after'-Wert durchlaufen lassen:
while date > after:
    ...


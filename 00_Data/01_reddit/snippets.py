import pandas as pd
import os

os.chdir('/Users/alex/PycharmProjects/d2d/tothemoon/00_Data/01_reddit')


df = pd.read_csv('AMC.csv', sep='|', lineterminator='\n')
df = df.drop_duplicates(subset='selftext')

# 25 categories of interest
out = df[['created_utc',
          'date',
          'ticker',
          'author',
          'author_fullname'
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
          'allow_live_comments'
          'all_awardings',
          'total_awards_received',
          'awarders',
          'gildings']]


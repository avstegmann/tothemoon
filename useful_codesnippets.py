import pandas as pd

df = pd.read_csv('submissions_reddit.csv', sep=',')
df = df.replace("\n", " ", regex=True)
df.to_csv('submissions_reddit.csv', sep='|', encoding='utf-8', index=False)

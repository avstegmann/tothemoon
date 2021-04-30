import pandas as pd
import spacy
import tqdm
import re
from string import punctuation
import os


os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/02_Reddit/archive')
df = pd.read_csv('full_no-dupes.csv', sep='|', lineterminator='\n')
os.chdir('/Users/alex/Universität St.Gallen/Data2Dollar - General/00_Data/02_Reddit')

nlp = spacy.load('en_core_web_lg')
print('spacy loaded')
PUNCTUATION = set(punctuation)
BLACKLIST = ['ev', 'covid', 'etf', 'nyse', 'sec', 'spac', 'fda', 'fed', 'treasury', 'eu', 'cnbc', 'faq', 'company',
             'otcbb', 'finra', 'wsb', 'ppp', 'msr', 'mso', 'dfv', 'otm', 'itm', 'fd', 'fyi', 'pe', 'eps', 'dow', 'tldr',
             'hodl', 'moon', 'td', 'ath', 'fomo', 'u s', 'eod', 'eow', 'hf', 'atm', 'cdc', 'fud', 'wsj', 'CNN', 'leaps',
             'usd', 'opec', 'ceo', 'cfo', 'tba', 'wtf']


def get_orgs(text):
    # https://github.com/jamescalam/transformers/blob/main/course/named_entity_recognition/xx_ner_reddit_freq_table.ipynb
    text = re.sub(r'[$]ROPE', '', text)

    org_list = re.findall(r'(?<=[$])[A-Z]{1,5}', text)

    text = re.sub('[\\d]', '', text)
    text = re.sub('Toronto NEO', '', text)
    for p in PUNCTUATION:
        text = text.replace(p, ' ')
    text = " ".join(text.split())

    doc = nlp(text)

    for entity in doc.ents:
        if entity.text.isupper() and len(entity.text) <= 5 and entity.label_ == 'ORG' and entity.text.lower() not in BLACKLIST:
            if entity.text == 'NOKIA':
                org_list.append('NOK')
            else:
                org_list.append(entity.text)
    org_list = list(set(org_list))
    return org_list


def main():
    master_list = []
    with tqdm.tqdm(total=df.__len__()) as pbar:
        for row in tqdm.tqdm(df.iterrows()):
            text = str(row[1].title) + ' ' + str(row[1].selftext)
            master_list.append(get_orgs(text))
            pbar.update(1)
    example = df
    example['ticker_mentions'] = master_list
    example.to_csv('ticker_search.csv', sep='|', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()

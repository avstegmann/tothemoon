import pandas as pd
import spacy
from collections import Counter
import re
from string import punctuation
import os


os.chdir('/Users/alex/Universität St.Gallen/STUD-DataToDollar - 02_Reddit')
df = pd.read_csv('full_no-dupes.csv', sep='|', lineterminator='\n')


nlp = spacy.load('en_core_web_lg')
PUNCTUATION = set(punctuation)
BLACKLIST = ['ev', 'covid', 'etf', 'nyse', 'sec', 'spac', 'fda', 'fed', 'treasury', 'eu', 'cnbc', 'faq', 'company',
             'otcbb', 'finra', 'wsb', 'ppp', 'msr', 'mso', 'dfv', 'otm', 'itm', 'fd', 'fyi', 'pe', 'eps', 'dow', 'tldr',
             'hodl']


def get_orgs(text):
    # https://github.com/jamescalam/transformers/blob/main/course/named_entity_recognition/xx_ner_reddit_freq_table.ipynb
    org_list = re.findall(r'(?<=[$])[A-Z]{1,5}', text)
    text = re.sub('[\\d]', '', text)
    text = re.sub('Toronto NEO', '', text)
    for p in PUNCTUATION:
        text = text.replace(p, ' ')
    text = " ".join(text.split())

    doc = nlp(text)

    for entity in doc.ents:
        if entity.text.isupper() and len(entity.text) <= 5 and entity.label_ == 'ORG' and entity.text.lower() not in BLACKLIST:
            org_list.append(entity.text)
    org_list = list(set(org_list))
    return org_list


def main():
    master_list = []
    for row in df.iterrows():
        text = str(row[1].title) + ' ' + str(row[1].selftext)
        master_list.append(get_orgs(text))
        print(row[0])
    example = df
    example['ticker_mentions'] = master_list
    example.to_csv('ticker_search.csv', sep='|', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()

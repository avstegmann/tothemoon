# Dieser Code sucht nach den Stichworten in Search Terms - Datenmenge wird vielleicht zu gross 'AMC','GME','TSLA',


import twint
import os

search_terms = ['BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','FORD','ASO','MVIS','AMD','GM','WIRE','M','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']

def jobone():
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = "2019-01-01 00:00:00"
        # c.Limit = 100 - viellecht müesse mer paar ihschränkige mache
        c.Store_csv = True
        c.Output = os.path.join('../02_Twitter/{}.csv'.format(search_terms[i]))

        twint.run.Search(c)

jobone()
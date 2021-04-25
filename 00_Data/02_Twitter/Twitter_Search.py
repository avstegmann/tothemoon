# Dieser Code sucht nach den Stichworten in Search Terms 


import twint
import os

search_terms = ['AMC', 'GME', 'BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','TSLA','FORD','ASO','MVIS','AMD','GM','WIRE','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']

def fun_mit_twitter():
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = "2016-01-01 00:00:00"
        # c.Limit = 100 - Einschränkungen werden nötig
        c.Store_csv = True
        c.Output = os.path.join('../02_Twitter/{}.csv'.format(search_terms[i]))

        twint.run.Search(c)

fun_mit_twitter()
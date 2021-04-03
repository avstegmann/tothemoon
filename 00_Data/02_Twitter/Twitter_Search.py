import twint
import csv

c = twint.Config()

c.Search = "GME OR Gamestop"
c.Since = "2019-01-01 00:00:00"
c.Output = "Twitter_1.csv"
c.Limit = 10

twint.run.Search(c)

print('Inder machen geile Codes')

import twint
import pandas
import datetime





#all_stocks = ['AMC', 'GME', 'BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','TSLA','FORD','ASO','MVIS','AMD','GM','WIRE','M','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']
#def scrape_by_stock(keywords, since, outfile):
#	unique_stocks = set(all_stocks) #To get unique cities of country
#	stocks = sorted(unique_stocks) #Sort & convert datatype to list
#	for stock in stocks:
#		print(stock)
 #       c.Search = keywords #search keyword
  #      c.Since = since
   #     c.Store_csv = True
   	#    c.Output = "./" + outfile
     #   c.Near = stock
      #  c.Hide_output = True
       # c.Count = True
       # c.Stats = True
        #c.Resume = 'resume.txt'
        #twint.run.Search(c)

#scrape_by_stock(all_stocks, '2021-04-1 15:55:00', 'Test.csv')

list_ = ['AMC', 'BB','KOSS','EXPR','ZOM','NOK','NAKD','PLTR','JAGX','SNDL','BBBY','TSM','CCIV','TSLA','FORD','ASO','MVIS','AMD','GM','WIRE','M','CURLF','NFLX','NCTY','TIRX','CTRM','RLX','EZGO','SRNE','CVM','LGND','FIZZ']


for i in list_:
    print(i)
    c = twint.Config()
    c.Search = i
    c.Pandas = True
    c.Since = "2021-03-01"
    c.Until = "2021-03-04"
    c.Custom_csv = ["id", "user_id", "username", "date", "tweet"]
    c.Output = "test.csv"
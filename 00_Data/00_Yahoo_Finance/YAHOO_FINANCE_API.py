from yahoo_finance import Ticker
from pprint import pprint

import yahoofinance as yf
import pandas as pd



import yfinance as yf

# get stock info

AMC_Entertainment_Holdings = Ticker('AMC')
Gamestop = Ticker('GME')
BlackBerry_Limited = Ticker('BB')
Koss_Corporation = Ticker('KOSS')
Express = Ticker('EXPR')
Zomedica_Corp = Ticker('ZOM')
Nokia_Corporation = Ticker('NOK')
Naked_Brand_Group_Limited = Ticker('NAKD')
Palantir_Technologies = Ticker('PLTR')
Jaguar_Health = Ticker('JAGX')
Sundial_Growers = Ticker('SNDL')
Bed_Bath_and_Beyond_Inc = Ticker('BBBY')
Taiwan_Semiconductor_Manufacturing_Company_Limited = Ticker('TSM')
Churchill_Capital_Corp_IV = Ticker('CCIV')
Tesla = Ticker('TSLA')
Forward_Industries = Ticker('FORD')
Academy_Sports_and_Outdoors = Ticker('ASO')
MicroVision = Ticker('MVIS')
Advanced_Micro_Devices = Ticker('AMD')
General_Motors_Company = Ticker('GM')
Encore_Wire_Corporation = Ticker('WIRE')
Macys = Ticker('M')
Curaleaf_Holdings = Ticker('CURLF')
Netflix = Ticker('NFLX')
The9_Limited = Ticker('NCTY')
Tian_Ruixiang_Holdings_Ltd = Ticker('TIRX')
Castor_Maritime_Inc = Ticker('CTRM')
RLX_Technology_Inc = Ticker('RLX')
EZGO_Technologies_Ltd = Ticker('EZGO')
Sorrento_Therapeutics = Ticker('SRNE')
CEL_SCI_Corporation = Ticker('CVM')
Ligand_Pharmaceuticals_Incorporated = Ticker('LGND')
National_Beverage_Corp = Ticker('FIZZ')


hist_AMC_Entertainment_Holdings = AMC_Entertainment_Holdings.history(period="max")


print(hist_AMC_Entertainment_Holdings)


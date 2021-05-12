# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:42:01 2020

@author: sneha
"""
#pip install yfinance

import yfinance as yf
import pandas as pd
import datetime

ticker = pd.read_csv('NYSE.csv')
ticker1d = ticker.Symbol[:]

start = datetime.datetime(2016,5,1)
end = datetime.datetime(2021,5,5)

price = yf.download('A')
price['ticker']= 'A'
price= price.truncate(before=-1, after=0)

print(price)

for t in ticker1d:
    p1 = yf.download(t,start=start,end=end,progress=False)
    print(t)
    p1['ticker']= t
    price = price.append(p1)
    
price.to_csv('E:\Price_Data\price_data_2021-05-05.csv')
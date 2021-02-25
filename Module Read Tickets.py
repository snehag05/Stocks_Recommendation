# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:42:01 2020

@author: sneha
"""
#pip install yfinance

import yfinance as yf
import pandas as pd
import mysql.connector
    

cnx = mysql.connector.connect(user='root', password='', 
                              host='localhost',
                              database='algee')

ticker = pd.read_csv('NYSE.csv')
ticker1d = ticker.Symbol[2601:3092]
price = yf.download('A')
price['ticker']= 'A'

for t in ticker1d:
    p1 = yf.download(t)
    p1['ticker']= t
    price = price.append(p1)
    
price.to_csv('A.csv')       


    
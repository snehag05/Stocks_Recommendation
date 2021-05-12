# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:20:20 2021

@author: sneha
"""
import mysql.connector
import Plot_and_ARIMA_fn as p
from pandas import DataFrame

def stock_list(risk_apt, yearly_inv, exp_return):
    cnx = mysql.connector.connect(host="localhost", user="root", db="nyse") 
    cur = cnx.cursor(buffered=True)
    #print(cnx.is_connected())
    query = "select ticker, short_name, daily_avg_returns, weekly_avg_returns, monthly_avg_returns, daily_volatility, weekly_volatility, monthly_volatility from security_master"
    cur.execute(query)
    sec_master = cur.fetchall()
    sec_m_DF = DataFrame(sec_master)
    sec_m_DF.columns=cur.column_names
    #print(sec_m_DF)
    #summary = sec_m_DF.describe()
    #print(sec_m_DF.describe())
    
    for index, row in sec_m_DF.iterrows():
        if (row["weekly_avg_returns"] >= exp_return and row["weekly_volatility"] <=risk_apt) :
            print(row["ticker"],row["weekly_avg_returns"],row["weekly_volatility"])
    while True: 
        print("Enter a ticker you are interested in:")
        ticker = input("ticker:")
        info_query = "select * from security_master where ticker='"+ticker+"';"
        #print(info_query)
        cur.execute(info_query)
        ticker_info = cur.fetchone()
        #print("ticker:"+str(ticker_info[0]))
        print("short name:"+str(ticker_info[1]))
        print("long name:"+str(ticker_info[2]))
        print("sector:"+str(ticker_info[3]))
        print("industry:"+str(ticker_info[4]))
        print("website:"+str(ticker_info[10]))
        print("dividend rate:"+str(ticker_info[11]))
        print("currency:"+str(ticker_info[13]))
        print("market cap:"+str(ticker_info[14]))
        
        p.d_plot(ticker)
        print("Do you want to see another ticker?")
        ans = input("Y/N?:")
        if ans=='Y':
            continue
        else:
            break
        
    cur.close()
    cnx.close()
    

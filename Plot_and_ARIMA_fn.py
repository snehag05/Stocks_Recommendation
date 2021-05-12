# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:55:42 2021

@author: sneha
"""

from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import mysql.connector
from matplotlib import pyplot

def d_plot(ticker):
    cnx = mysql.connector.connect(host="localhost", user="root", db="nyse") 
    cur = cnx.cursor(buffered=True)
    print(cnx.is_connected())
    
    query = "select * from weekly_data where ticker ='"+ticker+"';"
    #query = "select * from weekly_data where ticker ='JHS';"
    cur.execute(query)
    weekly_data = cur.fetchall()
    weekly_DF = DataFrame(weekly_data)
    #print(weekly_DF)
    weekly_DF.columns=cur.column_names
    weekly_DF.set_index('date')
    #weekly_DF.index = weekly_DF.index.to_period()
    #print(weekly_DF)

    weekly_DF.plot('date','price',title=ticker)
    #weekly_DF.plot('date','price',title='JHS')
    pyplot.gcf().canvas.set_window_title('Price History of '+str(ticker))
    pyplot.show()
    calc_ARIMA(weekly_DF)

#d_plot("JHS")
# https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
#https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html    
"""
A nonseasonal ARIMA model is classified as an "ARIMA(p,d,q)" model, where:
ARIMA models are, in theory, the most general class of models for forecasting a time series which can be made to be “stationary” by differencing (if necessary), perhaps in conjunction with nonlinear transformations such as logging or deflating (if necessary
p is the number of autoregressive terms,
d is the number of nonseasonal differences needed for stationarity, and
q is the number of lagged forecast errors in the prediction equation.
"""    

def calc_ARIMA(weekly_DF):
    # fit model
    model = ARIMA(weekly_DF.price, order=(2,0,0))
    model_fit = model.fit()
    # summary of fit model
    #print(model_fit.summary())
    # line plot of residuals
    #residuals = DataFrame(model_fit.resid)
    weekly_DF.price.plot()
    predicted = model_fit.predict(weekly_DF.price.size,weekly_DF.price.size+12)
    predicted.plot(title='Predicted Timeseries')
    pyplot.gcf().canvas.set_window_title('ARIMA')
    pyplot.show()
    # density plot of residuals
    #residuals.plot(kind='kde')
    #pyplot.show()
    # summary stats of residuals
    #print(residuals.describe())


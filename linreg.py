import pandas_datareader as web
import numpy as np
from sklearn.linear_model import LinearRegression

class Data:

    def __init__(self, stock, startdate, endate):
        df = web.DataReader(stock, data_source='yahoo', start=startdate, end=enddate)
        df = df['Adj. Close']


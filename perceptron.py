import tensorflow as tf
import csv
from tensorflow import keras
import pandas_datareader as web
import openpyxl as xl
import os
import numpy as np

class Data:

    def __init__(self, symbol, startdate, enddate):
        self.df = web.DataReader(symbol, data_source="yahoo", start=startdate, end=enddate)
        self.gdp_file = '/home/zach/PycharmProjects/stonks/datasets/gdp.csv'
        self.inflationusd_file = '/home/zach/PycharmProjects/stonks/datasets/inflationusd.csv'
        self.interest_rates_file = '/home/zach/PycharmProjects/stonks/datasets/interest_rates.csv'
        self.gdp = list(csv.reader(open(self.gdp_file)))
        self.inflationusd = list(csv.reader(open(self.inflationusd_file)))
        self.interest_rate = list(csv.reader(open(self.inflationusd_file)))
        self.unemploymentrates_us_workbook = xl.load_workbook('/home/zach/PycharmProjects/stonks/datasets/unemploymentrates_us.xlsx')
        self.sheet = self.unemploymentrates_us_workbook.get_sheet_by_name('BLS Data Series')
        self.unemploymentrates = []
        self.sheet = self.unemploymentrates_us_workbook.active
        for col in self.sheet.columns:
            self.unemploymentrates.append(col.value)
        print(self.unemploymentrates)

d = Data('TSLA', '2010-01-01', '2020-01-01')

model = tf.keras.Sequential([keras.layers.Dense(units=3, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')







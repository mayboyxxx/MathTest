#coding=utf-8
#-*- coding: UTF-8 -*-


import configparser
import  tushare as ts
import pandas as pd
import os
from datetime import datetime
import datetime
import time
#import MailSender
import seaborn as sns
import seaborn.regression as snre
import matplotlib.pyplot as plt
from matplotlib import style
import sys
import numpy as np
import  tushare as ts

def covTest1() :
    np.random.seed(12)
    X = np.random.randn(2000)
    Y = np.random.randn(2000)
    plt.scatter(X, Y)
    plt.show()
    print("correlation of X and Y is ")
    print(np.corrcoef(X, Y)[0, 1])


def covTest2(): #使用生成的相关序列，并加入正态分布的噪音
    X = np.random.randn(1000)
    Y = X + np.random.normal(0,0.1,1000)
    plt.scatter(X,Y)
    plt.show()
    print("correlation of X and Y is ")
    print(np.corrcoef(X, Y)[0, 1])


def covTest3():

    stock1 = ts.get_hist_data('600886', start='2017-01-05', end='2017-12-09')['close'].pct_change()[1:]
    stock2 = ts.get_hist_data('600993', start='2017-01-05', end='2017-12-09')['close'].pct_change()[1:]

    plt.scatter(stock1,stock2)
    plt.xlabel("stock 600886")
    plt.ylabel("stock 600993")
    plt.show()
    print("the corrlation for two stocks is: ")
    print(stock2.corr(stock1))

def covTest4():
    stock1 = ts.get_hist_data('600886', start='2017-01-05', end='2017-12-09')['close'].pct_change()[1:]
    stock2 = ts.get_hist_data('600993', start='2017-01-05', end='2017-12-09')['close'].pct_change()[1:]
    df = pd.read_csv("stock.csv")
    rolling_cor = pd.rolling_corr(stock1,stock2,60)

    df['date'] = df['date'].astype(np.datetime64) #数据格式转换
    rolling_cor.index = df['date'][1:]
    plt.plot(rolling_cor)
    plt.xlabel('day')
    plt.ylabel('60-day Rolling Correlation')
    plt.show()




covTest4()

#print(ts.trade_cal())

#生成数据文件
#df = ts.get_hist_data('600886',start='2017-01-05', end='2017-12-09')
#df.to_csv("stock.csv")
#df = pd.read_csv("stock.csv")
#df['date'] = df['date'].astype(np.datetime64)
#print(df['date'])

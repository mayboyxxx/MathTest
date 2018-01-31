#coding=utf-8
#-*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
from statsmodels import regression
import statsmodels.api as sm
import pandas_datareader.data as web
import math
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

import seaborn

import tushare as ts
GUOTOU_CODE = "600886"
GUANGQI_CODE = "601238"
MAYINGLONG_CODE = "600993"

def linreg(X,Y):
    # 运行线性回归
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    a = model.params[0]
    b = model.params[1]
    X = X[:, 1]

    # 返回信息并绘图
    X2 = np.linspace(X.min(), X.max(), 100)
    Y_hat = X2 * b + a
    plt.scatter(X, Y, alpha=0.3) # 显示原始数据
    plt.plot(X2, Y_hat, 'r', alpha=0.9);  # 添加拟合直线
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.show()
    return model.summary()



#X = np.random.rand(100)
#Y = np.random.rand(100)
#linreg(X,Y)

stockA = ts.get_hist_data(MAYINGLONG_CODE,'2017-07-17','2018-01-17')['close']
stockSH = ts.get_hist_data('sh','2017-07-17','2018-01-17')['close']
r_stockA = stockA.pct_change()[1:]
r_stockSH = stockSH.pct_change()[1:]

#linreg(r_stockSH.values,r_stockA.values)

seaborn.regplot(r_stockSH.values,r_stockA.values)
plt.show()
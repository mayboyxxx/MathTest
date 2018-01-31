#coding=utf-8
#-*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import math
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

np.random.seed(121)

X = np.random.randint(100,size=20)

print(X)

X = np.sort(X)

print(X)

print(np.mean(X))

print('Range of X: %s' %(np.ptp(X)))

mu = np.mean(X)
abs_dispersion = [np.abs(mu - x) for x in X]
#print(abs_dispersion)

MAD = np.sum(abs_dispersion)/len(abs_dispersion)
print("X的平均绝对差:",MAD)
print("X的方差:",np.var(X))
print("X的标准差:",np.std(X))


k = 1.25 # 随便举的一个k值
dist = k*np.std(X)
l = [x for x in X if abs(x - mu) <= dist]
print('k值', k, '在k倍标准差距离内的样本为:', l)
print('验证', float(len(l))/len(X), '>', 1 - 1/k**2)


#半方差 ，金融系统  低于平均值部分的方差

lows  = [(mu-x)**2 for x in X if x<= mu]
highs  = [(mu-x)**2 for x in X if x>= mu]

halfVar = np.sum(lows)/len(lows)
highhalfVar = np.sum(highs)/len(highs)


print("半方差 ：",halfVar)
print("半标准差",np.sqrt(halfVar),"lows 个数：",len(lows))
print("高半标准差",np.sqrt(highhalfVar))


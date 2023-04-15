#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv(r"C:\Users\Admin\Desktop\Shwetha V\ITK SDP\homeinfo.csv")
df

plt.scatter(df.area,df.price)

plt.xlabel('area (sq.ft)')
plt.ylabel('price (Rs)')
plt.scatter(df.area,df.price,color='red',marker='+')

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
reg.predict([[3300]])



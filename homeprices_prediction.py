#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[27]:


df=pd.read_csv(r"C:\Users\Admin\Desktop\Shwetha V\ITK SDP\homeinfo.csv")
df


# In[ ]:





# In[ ]:





# In[28]:


plt.scatter(df.area,df.price)


# In[30]:


plt.xlabel('area (sq.ft)')
plt.ylabel('price (Rs)')
plt.scatter(df.area,df.price,color='red',marker='+')


# In[31]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
reg.predict([[3300]])


# In[ ]:





# In[ ]:





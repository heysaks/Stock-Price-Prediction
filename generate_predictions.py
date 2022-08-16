#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('aimport', 'data_creater')
get_ipython().run_line_magic('aimport', 'model')
get_ipython().run_line_magic('autoreload', '1')

from model import Predictor
from data_creater import *


# In[2]:


tickers = ['FB','GOOG','AAPL','IBM']


# In[3]:


start_date = '20161101' 
end_date = '20181031'
#download quotes from yahoo and save to directory
for ticker in tickers:
    Predictor.download_prep(ticker,start_date,end_date)


# In[4]:


stock_1 = tickers[0]
print("***  Closing price prediction for {} *** ".format(stock_1))
pred = Predictor(stock_1)
pred.select_model(verbose=1)
pred.graph()


# In[5]:


for ticker in tickers[1:]:
    print("***  Closing price prediction for {} *** ".format(ticker))
    pred = Predictor(ticker)
    pred.select_model(verbose=2)
    pred.graph()


# In[ ]:





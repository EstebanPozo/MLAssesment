#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

def df2c(df, window_size=5):
    df2np=df.to_numpy()
    X=[]
    y=[]
    for i in range(len(df2np)-window_size):
        row=[[a] for a in df2np[i:i+window_size]]
        X.append(row)
        label=df2np[i+window_size]
        y.append(label)
    return np.array(X), np.array(y)


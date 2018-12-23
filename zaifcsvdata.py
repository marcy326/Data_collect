# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:25:52 2018

@author: marcy

zaifJPY.csvを分割
"""

import pandas as pd

dtyp = {'time': 'int32', 'price':'int32', 'amount': 'float32'}
btc = pd.read_csv("data/zaifJPY.csv", names=("time", "price", "amount"), dtype=dtyp)

a = range(0, len(btc.index) + 500000, 500000)

#for i in range(len(a)-1):
for i in range(3):
    btc[a[i]:a[i+1]].to_csv("data/zaifJPYtest-" + str(i) + ".csv")
    print(i)


# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:02:00 2018

@author: marcy

生データを1分足のデータにする
"""

import pandas as pd
import time


csv = pd.DataFrame()

timest = time.time()
for i in range(117):
    btc = pd.read_csv("data/zaifJPY-" + str(i) + ".csv", index_col=0, parse_dates=True)
    
    #時間をインデックスに指定
    btc.set_index('time', inplace=True)
    
    #UnixTimeを日本時間に変換
    btc.index = pd.to_datetime(btc.index, unit='s')
    btc.index = btc.index.tz_localize('UTC').tz_convert('Asia/Tokyo')

    #1分でリサンプリングして、終値をとる
    btc = btc.resample('1T').last()
    csv = pd.concat([csv, btc])
    print(i)

csv = csv.price.fillna(method='ffill')
csv = csv['2017-08-04':]

csv.to_csv("data/time/zaifJPYprice1min.csv")
print("done!")

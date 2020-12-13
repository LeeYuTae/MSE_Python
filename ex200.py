#!/usr/bin/env python
# coding: utf-8

# In[28]:


ohlc = [["open", "high","low","close"],
        [100,110,70,100],
        [200,210,180,190],
        [300,310,300,310]]
total_profit = 0
for day_price in ohlc[1:]: # [1:] = 1 -> [100,110,70,100] ~ : -> [300,310,300,310]
    profit = (day_price[0] - day_price[3]) # profit = 0 . 10 . -10
    total_profit += profit # total_profit += profit -> total_profit = total_profit + profit

print(total_profit)
#답 :0


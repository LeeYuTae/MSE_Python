#!/usr/bin/env python
# coding: utf-8

# In[1]:


low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):       # len(low_prices) = 5 
    volatility.append(high_prices[i] - low_prices[i]) # append : 어떤 값을 추가 -> high_prices[i] - low_prices[i] 의 값을 volatility 에 추가함
print(volatility)
#답 :[50, 100, 30, 80, 0]


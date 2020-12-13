#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import : 파이썬의 외장 함수나 다른 사람이 만든 모듈을 사용하기 위해 불러오는 것.
import requests  
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] # btc : bitcoin , 컴퓨터 용어 아님

변동폭 = float(btc['max_price']) - float(btc['min_price']) # float : 실수
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#답 :상승장


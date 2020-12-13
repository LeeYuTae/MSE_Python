#!/usr/bin/env python
# coding: utf-8

# In[25]:


class stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per  = per
        self.pbr  = pbr
        self.배당수익률 = 배당수익률
# 생성자를 정의하는 과정

종목 = [] # List 생성

삼성   = stock("삼성전자", "005930", 15.79, 1.33, 2.83) # 괄호안은 순서대로 (name, code, per, pbr, 배당수익률)
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)
# stock 클래스의 객체를 만드는 과정 

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
    
# 답:005930 15.79
#   :005380 8.7
#   :066570 317.34


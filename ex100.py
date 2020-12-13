#!/usr/bin/env python
# coding: utf-8

# In[4]:


# zip : 두개의 리스트 또는 튜플을 0번은 0번끼리 1번은 1번끼리 n번은 n번 끼리 묶음
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10800, 11000]
close_table = dict(zip(date, close_price)) # dict : {} , 키와 값을 저장하는 것이 핵심.
print(close_table)
#답 :{'09/05': 10500, '09/06': 10300, '09/07': 10800, '09/08': 11000}


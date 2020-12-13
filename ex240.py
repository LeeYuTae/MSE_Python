#!/usr/bin/env python
# coding: utf-8

# In[1]:


# return : 함수값 반환
def 함수0(num):
    return num * 2

def 함수1(num):
    return 함수0(num + 2)

def 함수2(num):
    num = num + 10
    return 함수1(num)  

c = 함수2(2)      
print(c)           
# 함수2(2) -> num = 2
# num = 2 +10 -> 함수1(12) -> num = 12
# 함수0(12+2) -> 함수0(14) -> num = 14
# 14 * 2 = 28

#답 :28


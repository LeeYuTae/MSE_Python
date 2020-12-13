#!/usr/bin/env python
# coding: utf-8

# In[2]:


class OMG :
    def print():
        print("Oh my god")
        
        mystock = OMG()
    mystock.print()
# NameError :name 'mystock' is not defined


# In[7]:


class OMG :
    def print(self): # 에러가 발생한 이유 :인자(self)가 필요함
        print("Oh my god")
        
mystock = OMG()
mystock.print()     # OMG.print(mystock) 와 같음.
# 답 :Oh my god


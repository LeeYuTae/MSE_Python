#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_max(a,b,c):
    max_val = 0
    # max(1,10,5) 인 경우로 설명
    if a > max_val:
        max_val = a  # a=1 > max_val=0  - > max_val = 1
    if b > max_val:  
        max_val = b  # b=10 > max_val=1 - > max_val = 10
    if c > max_val:
        max_val = c  # max_val=10 > c=5 - > max_val = 10
    print(max_val)
    
print(max(1,10,5))
#답 :10


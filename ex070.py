#!/usr/bin/env python
# coding: utf-8

# In[9]:


# sort , sorted : 리스트 정렬방법
data = [2,4,3,1,5,10,9]
data.sort()              # sort : 기존에 리스트 값을 순서대로 정렬한다. 새로운 변수 선언 필요 X
print(data)
#답 :[1, 2, 3, 4, 5, 9, 10]


# In[10]:


data1 = sorted(data)    # sort : 기존에 리스트 값은 변화시키지 않고 순서대로 정렬한 리스트를 반환. 새로운 변수 선언 필요
print(data1)
#답 :[1, 2, 3, 4, 5, 9, 10]


#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Tuple : () , 리스트와 달리 한번 생성된 값을 변경할 수 없다.
data = tuple(range(2,100,2)) # range(a,b,c) : a 부터 (b-1) 까지 2씩 커진다.
print(data)
#답 :(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)

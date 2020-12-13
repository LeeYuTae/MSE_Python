#!/usr/bin/env python
# coding: utf-8

# In[2]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000} # key : 빵빠레, 월드콘, 메로나  value : 1800, 1500, 1000 
icecream['누가바'] # 에러가 나오는 이유:dict 의 key (폴라포,빵빠레,월드콘,메로나) 중에 없는 누가바를 사용했기 때문
# KeyError: '누가바'


# In[3]:


print(icecream['빵빠레'])
print(icecream['월드콘'])
#답 :1800
#    1500


#!/usr/bin/env python
# coding: utf-8

# In[5]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    split = i.split(".")             # split : 분리  #i.split : i 를 .을 기준으로 분리
    if(split[1] == "h") or (split[1] == "c"): # .을 기준으로 나뉜것들 중에서 1번째자리의 글자가 h 이거나 c인 원소 출력 ex) intra.c 에서 .을 기준으로 . = 0번째 c = 1번째 이므로 출력됨
        print(i)    
#답 :intra.h
#   :intra.c
#   :define.h


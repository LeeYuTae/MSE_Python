#!/usr/bin/env python
# coding: utf-8

# In[4]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
과일 = input("좋아하는 과일은?")   # input : 입력값을 받아주는 함수. 숫자나 문자열을 입력하고 싶을 때 사용
if 과일 in fruit.values():         # fruit,values : 딸기 , 토마토 , 사과
    print("정답입니다.")
else:
    print("오답입니다.")           # 바나나 는 fruit 에 없으니 "오답입니다." 가 출력됨
#답 :좋아하는 과일은?바나나
#    오답입니다.


#!/usr/bin/env python
# coding: utf-8

# In[5]:


class 부모:
    def __init__(self):    # __init__ : 클래스가 인스턴스화 될 때 호출. 객체 생성 방법을 제어
        print("부모생성")
        
class 자식(부모):
    def __init__(self):    # 생성자 호출
        print("자식생성")
        super().__init__() # 부모 클래스의 생성자를 명시적으로 호출함. ()안에 self 적을 필요 없음.
                           # super : 상속 한 클래스의 함수를 추가로 적지 않고도 사용할 수 있음
            
나 = 자식()
#답 :자식생성
#   :부모생성


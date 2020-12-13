#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1(): # def : 함수를 만드는 명령어
    print("A")
    
def message2():
    print("B")
    
def message3():
    for i in range (3):      # message2() = B 이므로 B 출력한다음 print("C") 로 인해 C 출력. 이를 3번 반복
        message2()
        print("C")
    message1()               # for 문을 3번 반복한 후에 message1() = A 출력
    
message3()
#답 :B
#   :C
#   :B
#   :C
#   :B
#   :C
#   :A


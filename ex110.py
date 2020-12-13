#!/usr/bin/env python
# coding: utf-8

# In[5]:


if True:# 1번
    if False:# 2번
        print("1")
        print("2")
    else:# 3번          # 조건(2번)이 거짓(False)이므로 "3"이 출력됨
        print("3")
else:# 4번
    print("4")          # 조건(1번)이 참(True)이므로 "4"는 출력되지 않음
print(5)               # if 문에 관계없이 그냥 실행
#답 :3
#   :5


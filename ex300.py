#!/usr/bin/env python
# coding: utf-8

# In[2]:


per = ["10.31", "", "8.00"]

for i in per:
    try:                  # try : 실행코드 
        print(float(i))   # float : 실수
    except:              # except : 예외가 발생했을 때 수행할 코드
        print(0)
    else:                # else : 예외가 발생하지 않았을때 수행할 코드
        print("clean data")
    finally:             # finally : 예외 발생 여부와 상관없이 항상 수행할 코드
        print("변환 완료")
        
# 10.31 - > 에러 발생 X - > clean data 출력 - > 변환 완료 출력
# 0     - > 에러 발생 O - > 0 출력 - > 변환 완료 출력
# 8.00  - > 에러 발생 X - > clean data 출력 - > 변환 완료 출력

#답 :10.31
#   :clean data
#   :변환 완료
#   :0
#   :변환 완료
#   :8.0
#   :clean data
#   :변환 완료


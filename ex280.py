#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random

# class variable
    # Account 클래스로부터 생성된 계좌 객체의 개수를 저장
class Account:
    account_count = 0
    
    def __init__(self,name,balance):
        self.deposit_count = 0
        self.deposit_log   = []   # 객체가 생성될 때 
        self.withdraw_log  = []   # 이 두개의 mt list가 생성이 됨.
        
        self.name    = name
        self.balance = balance
        self.bank    = "sc은행"
        
        num1 = random.randint(0,999) # 0 <= i <= 99 범위안의 임의의수 i 값 출력
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3) # zfill : zero fill method -> 자리수를 채움  ex) 99 를 zfill(4)) 하면 99 -> 0099
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3 # 계좌번호 
        Account.account_count += 1
        
    #class method
    def get_account_num(cls):
        print(cls.account_count)
        
    def deposit(self, amount):  # amount : 입금액
        if amount >= 1: 
            self.deposit_log.append(amount) # 입금을 할때마다 입금내역을 저장
            self.balance += amount
            
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                #이자 지급 조건 : 입금 내역이 5의 배수로 진행되었을때
                self.balance = (self.balance * 1.01)
                #이자 지급 방법
                
    def withdraw(self,amount):
        if self.balance > amount:
            self.withdraw_log.append(amount) # 출금을 할때마다 출금내역을 저장
            self.balance -= amount
                
    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", self.balance)
            
    def withdraw_history(self):
        for amount in self.withdraw_log: #출금내역 
            print(amount)
                
    def deposit_history(self):
        for amount in self.deposit_log:  #입금내역
            print(amount)

k = Account("Kim", 1000) # 처음에 1000원을 넣음.
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

#답 :100
#   :200
#   :300
#   :100
#   :200


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:39:04 2019

@author: owner
"""
""""
a,b =1,10
if a>b:
    print("a>b")
elif a<b:
    print("a<b")
else:
    print("a=b")
    
    
a,b=1,10
max= a if (a>b) else b
print(max)    
    


if 'a' in ['b','c','a']:
    print("a in the list")
else: print ("a not in the list")        

a=1000
b=330
print("A") if a>b else print("=") if a==b else print("B")
"""

'''
a,b=input("insert 2 num??").split()
print(a,b) if int(a)<int(b)  else print(b,a)
'''
"""
name,age=input("insert name and age ??\t").split()
if int(age) < 18:
    print("Under Age")
    avg=input("plece enter your school avg:\t")
    if int(avg)>=90:
        print("Excellent avg")
    elif int(avg)>=50 and int(avg)<=90:
        print("passed")
    else:
        print("Faild")
else:
    print("Adult")
    job=input("pleace enter your job title:\t")
    print("age:",age,"\t","name:",name,"\t","job:",job)
"""
"""        
for o in range(-1,-7,-2):
    print(o)
 """
'''
while True:
    a=int(input(">"))
    if a==1:
        break
    print(a)
'''
"""   
for a in range(10):
    print("*")
 
for a in range(20):
    print("*",end='')

y="*"
for a in range (8):
    print(y)
    y=y+"*"
"""
'''
y="*"
for a in range(8):
    for i in range(a):
        print(y,end="")
    print()
 '''       
'''
for a in range(9):
    for i in range((9-a)):
        print(" ",end="")
    for x in range(a):
        print("*",end="")
    print()
  '''
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")  
        






  
    

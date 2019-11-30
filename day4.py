#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:33:52 2019

@author: owner
"""
'''
def name(a):
    print(a)


name("yasmin")


def my_function(x):
    for x in x:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def y(*num):
    sum=0
    
    for n in num:
        sum=sum+n
    print("sum=", sum)
    
    

y(1,5,8)
y(1,8,9,6)


def u(*s,a):
    print(a)
    for t in s:
        print(t)

u(1,5,8,a=9)

def t(a,s,d):
    print(a)
    print(s)
    print(d)

l=[2,8]
t(1,*l)  


def u(**k):
    for key,value in k.items():
        print(key,"==",value)
 
u(e=1,r=6,t=9)



x = "awesome"
def myfunc():
    print("Python is " + x)


myfunc()
print("Python is " + x)



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(2956))

usm=lambda x,c,v: x+c-v
print(usm(5,2,3))

print ((lambda x, y, z=3: x + y + z)(1, 2,2))


MyList = [0,1,2,3,4,10,13,22,25,100,120]
print("squared List:", map(lambda x: x**2, MyList[0])) 
    
   

MyList = [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers = list(filter(lambda x: x % 2, MyList))
print(odd_numbers)

even_numbers = list(filter(lambda x: not(x % 2), MyList))
print(even_numbers)



scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
x= list((lambda y:y>75),scores)
print(y)



my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5,8]
l = [1,2,3,"y","e","w"]

results = list(zip(my_strings, my_numbers,l))
print(results)
'''
from functools import reduce
x= reduce(lambda a,b: a+b,[23,21,45,98])
print(x)



   
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:49:48 2019

@author: owner
"""

#print ("strip :", 'vvvvv    world '.strip() )
'''
s1="hello orange academy"
print(s1)
print(s1[0])
print(s1[-2])
print(s1[2:10])
print(s1[5:])
print(s1*2)
print(s1.capitalize())
print(s1.upper())
print (s1.center(20))
print (s1.replace('Orange', 'Amman'))
print (' world'.strip() )
s2='#'.join(['hello','Orange'])
print(s2)
'''
'''
d=s1.split()
for y in range(len(d)):
    print(d[y].capitalize())

p=['Apple', 1, 1.2222, 10, 20, ['Orage', 3]]
print("Orage" in p )
'''
'''
d=s1.split()
for y in d:
    print(y.capitalize())


print(s1+s2)
'''
'''
a = "Apple"
my_list1= list(a)
print (my_list1)
i1= my_list1
print(i1)

my_list1=[1,2,1,3,4,1]
print (my_list1.index(5))


list1=[1,20,-1,0,1000]
list2=[23,546]
list1.extend(list2)
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))
print(sorted(list1))
list1.sort()
print(list1)
list1.pop()
print(list1)
p=list1.copy()
print(p)

i=(4,8,9,2)
print(type(i))
print(i)

s1={1,2,6,8}
s2={1,5,6,4}
print(s1-s2)
print(s1^s2)
'''
a={
   "firstname":"yasmin",
   "lastname":"alhajjaj",
   "age":23,
   }

for x in a:
    print(x,":",a[x])
'''   
for x in a.values():
    print(x)
'''
for x,y in a.items():
    print(x,y)














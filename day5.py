#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:52:39 2019

@author: owner


class hello:
    def hi(self):
        print("hello")
        
        
p= hello()
p.hi()        



class Person:
    
    def __init__(self, name):
        self.name = name
        
    def whoami( self ):
        return "I am " + self.name
    
    def __del__( self ):
        print ( "I have been deleted")
        
     
p1 = Person('tom')
print(p1.whoami())
print(p1.name)
#del p1


class Vehicle:
    def __init__(self):
        print('Vehicle created.')

    def __del__(self):
        print('Destructor called, vehicle deleted.')

car = Vehicle()
#del car



class Encapsulation():
    def __init__(self, a, b, c):
        self.Apublic = a
        self._Bprotected = b
        self._Cprivate = c
    def setprivate(self):
        self.__Cprivate = 19
    
    def getprivate(self):
        return self.__Cprivate

x = Encapsulation(11,13,17)
print ( x.Apublic )
print ( x._Bprotected )
#print ( x._Cprivate) #->>>> Error
x.setprivate()
print ( x.getprivate())




class A(object):
    def __init__(self):
        print("world")
class B(A):
    def __init__(self):
        A.__init__(self)
        print("hello")
        super().__init__(self)
b1=B()



class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius

    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle )

c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + 8
print(c3.getRadius())
c4 = c3 + 8
print(c4.getRadius())





class Dog:
    kind = 'canine' # class variable shared by all instances"
    def __init__(self, name):
        self.name = name
# instance variable unique to each
#instance
d = Dog('Fido')
e = Dog('Buddy')
print( d.kind)
print(e.kind)
print(d.name )
print(e.name )
d.kind = "e"
print( d.kind)
print(e.kind)


"""

class Dog:
    tricks = [] # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print( d.tricks )
# unexpectedly shared by all dog
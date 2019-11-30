#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:01:23 2019

@author: owner
"""

import numpy as np
import matplotlib.pyplot as plt


b = np.array([1, 4, 7, 5])
#print(b)



c = np.array([ [1, 4, 7, 5],[2, 8, 3, 2]])
#print(c)

p=np.ones((2,5), dtype=np.int16)
#print(p)



a =np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]])
#print (np.sort(a,kind='quicksort') )
#print (np.sort(a,kind='heapsort') )



"""
f=[1, 2, 8, 4,5,6]
plt.plot(f)



plt.style.use('ggplot')
x=[1, 2, 3, 4,5,6]
y=[1, 4, 9, 16,0,30]
plt.plot(x,y )
plt.ylabel('Y Numbers')
plt.xlabel('X Numbers')



import numpy as np
import matplotlib.pyplot as plt
def p1(x): return x**4 - 4*x**2 + 3*x
def p2(x): return np.abs(10*x) * 10
X = np.linspace(-3, 3, 100)
plt.plot( X,p1(X), X,p2(X))
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
plt.plot(x, y)

plt.show()






import numpy as np
import matplotlib.pyplot as plt
n = 1024
X = np.random.normal(0,8,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.show()


"""


import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3,
'g^')
plt.show()
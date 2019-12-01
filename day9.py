#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sun Dec  1 09:28:16 2019

@author: owner

import statistics as st
import random
import math


x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

print("////////////////////////////")
print( random.random() )
print (random.randrange(100))
print (random.choice (['Jordan', 'USA', 'UK']))
print (random.sample (range (100), 5) )
print (random.choice('abcdefghij'))
items = [11, 12, 30, 14, 35, 66, 17]
random.shuffle(items)
print( items)
print (random.randint(10, 20) )
print (random.randrange(0, 101, 2))
print (random.uniform(1, 100))



n = 100.08
print(math.floor(n))
print(math.ceil(n))

#Doctest lib
import doctest
def sum (a,b):
    """
    Calculates the sum of a and b
    >>> sum (1,1)
    2
    >>> sum(1,-1)
    0
    >>> sum (-1,-1)
    -2
    >>> sum(0,-10)
    -10
    >>>
    """
    return a+b
if __name__=="__main__":
    doctest.testmod(verbose=True)

from PIL import Image

im=Image.open("cat.jpeg")
print(im.format, im.size, im.mode)
im.show()

from PIL import Image,ImageFilter

im=Image.open("cat.jpeg")

blu=im.filter(ImageFilter.BLUR)
blu.show()
blu.save("catblu.png")




from PIL import Image

size=(128,128)
saved="catthumb.jpeg"

try:
    im=Image.open("cat.jpeg")
except:
    print('Uneble')

im.thumbnail(size)
im.save(saved)
im.show()

from PIL import Image,ImageFilter
im=Image.open("cat.jpeg")
con=im.filter(ImageFilter.CONTOUR)
con.show()

enh=im.filter(ImageFilter.EDGE_ENHANCE)
enh.show()

find=im.filter(ImageFilter.FIND_EDGES)
find.show()


smo=im.filter(ImageFilter.SMOOTH)
smo.show()


crop=im.crop((0,0,50,50))
crop.show()

resi=im.resize((500,500))
resi.show()

from PIL import Image
from PIL import ImageDraw

im=Image.open("cat.jpeg")
draw=ImageDraw.Draw(im)
draw.line((0,0)+im.size, fill=(255,255,255))
draw.line((0,im.size[1],im.size[0],0), fill=(255,255,255))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'Asma',fill=(225,225,0))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2-60),'Image',fill=(225,225,0))
im.show()


imagerot=im.rotate(90)
imagerot.show()

imgflip=im.transpose(im.FLIP_TOP_BOTTOM)
imgflip.show()


'''













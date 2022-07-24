# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:15:23 2022

@author: tcran
"""
import random
import numpy as np 

class circle():
    def __init__(self,cx=0,cy=0,r=1):
        self.cx = cx
        self.cy = cy
        self.r = r
    
    def area(self,r = 1):
        return np.pi*r*r
    
    def circum(self):
        return 2*np.pi*self.r
    
    def inside(self,x,y):
        distance = (self.cx-x)**2 + (self.cy-y)**2
        
        if distance <= self.r:
            print('point is inside the circle')
        else:
            print('point is outside of the circle')
        
    
        
a = circle()

print(a.area())
print(a.circum())
print(a.inside(1.5, 1.5))
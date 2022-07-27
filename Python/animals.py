# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:37:15 2022

@author: tcran
"""

import random 
class animal():
    def __init__(self,x=0,y=0):
        self.x= x
        self.y = y
        self.hitpoints = 100
        
    def move(self,x_min,y_min,x_max,y_max):
        a = random.randint(1,4)
        
        if a == 1:
            self.y +=1
        elif a == 2:
            self.x += 1
        elif a == 3 :
            self.y -= 1 
        elif a == 4 :
            self.x -= 1
        
        if self.x <= x_min :
            self.x = x_min 
        if self.x >= x_max:
            self.x = x_max
        if self.y <= y_min:
            self.y = y_min 
        if self.y >= y_max :
            self.y = y_max
        
        
        
class predator(animal):
    pass

class prey(animal):  
    pass       
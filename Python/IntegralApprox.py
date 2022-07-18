# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:08:42 2022
Code to approximate an integral 

@author: tcran
"""

import numpy as np
def trapezoid(f,a=0,b=1,n=100):
    h = (b-a)/n     #The length of each slice
    total = 0.0     # holds the values of the sum 
    if n <= 0:
        raise ValueError('n is not positive', n)
        
    for i in range(1, n):
        total += f(a+i*h)
    total *= 2.0
    total += f(a) + f(b)
        
    return (total*h)/2.0
        
             

 
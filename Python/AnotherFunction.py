# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:31:53 2022

@author: tcran
"""
import math
import matplotlib.pyplot as plt 

def sum2(N,x=[]):
    
    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(N+1):
            total += ((-1)**N)*(x[i]**(2*n))/(math.factorial(2*n))
            
        x_totals.append(total)
    
    #plt.plot(x,x_totals)
    return x_totals


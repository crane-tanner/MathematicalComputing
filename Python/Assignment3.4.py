# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:01:32 2022

@author: HP
"""
import numpy as np 
import matplotlib.pyplot as plt 

def midpoint(f,a=0,b=1,n=10):
    total = 0
    length = (b-a)/n
    x = np.arange(a,b+length,length)
    for i in range(n):
        total += f((x[i] + x[i+1])/2)*length
        
    plt.plot(x,f(x))
    
    riemannx = np.arange(a,b,length)
    plt.bar(riemannx,f(riemannx), align ='center', color='orange',edgecolor='blue',
            width=length, alpha =0.5)
    plt.xlim(a,b)
    plt.show()
    print(total)
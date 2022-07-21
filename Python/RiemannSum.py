# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:37:44 2022

@author: tcran
"""
import numpy as np 
import matplotlib.pyplot as plt 


# def riemann(f,a =0,b=1,n=100):
#     if (n <= 0):
#         raise ValueError('n is not positive', n)
    
#     length = (b-a)/n
#     x = np.arange(a,b+length,length)
#     plt.plot(x,f(x))
#     plt.show()
    
def riemannplot(f,a =0,b=1,n=10):
    length = (b-a)/n
    x = np.arange(a,b+length,length)
    plt.plot(x,f(x))
    
    riemannx = np.arange(a,b,length)
    plt.bar(riemannx,f(riemannx), align ='edge', color='orange',edgecolor='blue',
            width=length, alpha =0.5)
    plt.xlim(a,b)
    plt.show()
    
def f(x):
    return x*x


   
   
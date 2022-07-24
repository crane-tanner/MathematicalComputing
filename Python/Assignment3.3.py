# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:55:37 2022

@author: HP
"""

import matplotlib.pyplot as plt 


def _sum(N=10, x=[4,5,6,7,8]):
    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(1,N+1):
            total += (x[i]**n)/n
            
        x_totals.append(total)
    
    plt.plot(x,x_totals)
    return x_totals


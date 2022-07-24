# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:31:10 2022

@author: HP
"""
#problem 2 
import matplotlib.pyplot as plt


def sum_1(N=100):
        x_totals = []
        total = 0
        for n in range(1,N+1):
            total += (-1)**(n+1)*(1/n)
            x_totals.append(total)
       
        plt.plot(range(1,N+1),x_totals)
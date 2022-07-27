# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:32:38 2022

@author: tcran
"""
import matplotlib.pyplot as plt 
from matplotlib import animation 
import numpy as np 

## Main goal: create a plot that is a sprial coming out from (0,0) 

#1) Make an initial empty plot with axes defined 
#make x,y axis from -50 to 50 
figure = plt.figure()
ax = plt.axes(xlim=(-50,50),ylim=(-50,50))
line, = ax.plot([],[], lw=2)
#2) make a function that creates our empty line vector 
def func():
    line = ax.set_data([],[])
    return line, 

#3 Make our parametric equation that we are going to plot 

#4) Add each new step of our parametric equation to equations array 
xarray = []
yarray = []
#5) Create animation 
def animate(i):
    t = 0.1*i
    x = 1-t*np.cos(t)
    y = 1+t*np.sin(t)
    
    xarray.append(x)
    yarray.append(y)
    
    line.set_data(xarray,yarray)
    
    return line, 
    
    

## Plot animation 
anim = animation.FuncAnimation(figure,animate,frames = 500,interval = 20)
plt.show()


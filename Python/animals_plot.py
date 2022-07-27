# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:48:50 2022

@author: tcran
"""

import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation 
import animals 

def animate(frame_number):
    for an in pop: 
        an.move(x_min,x_max,y_min,y_max)
    
    
    
    
    d.set_data([animal.x for animal in pop if 
              animal.__class__ is animals.prey],
              [animal.y for animal in pop if
              animal.__class__ is animals.prey])

    c.set_data([animal.x for animal in pop if 
              animal.__class__ is animals.predator],
              [animal.y for animal in pop if
              animal.__class__ is animals.predator])
    e.set_data([animal.x for animal in pop_dead],[animal.y for animal in pop_dead
           ]) 
    





# set space limits 
x_max = 25
x_min = 0 
y_max = 25 
y_min = 0

## number of frames to simulate 
frames = 1000 

## population of our model 
num_prey = 25 
num_predator = 5 


pop = [animals.prey(x_max*np.random.uniform(0,1),
       y_max*np.random.uniform(0,1))
       for i in range(num_prey)] \
    + [animals.predator(x_max*np.random.uniform(0,1),
    y_max*np.random.uniform(0,1)) for i in range(num_predator)]
    
    
pop_dead = []

## set Ax length and get current figure 
ax = plt.axes(xlim=(x_min,x_max),ylim=(y_min,y_max))
fig = plt.gcf()

## plot first instance 
d, = plt.plot([animal.x for animal in pop if 
animal.__class__ is animals.prey],
[animal.y for animal in pop if
animal.__class__ is animals.prey], 'bo', markersize = 5)

c, = plt.plot([animal.x for animal in pop if 
              animal.__class__ is animals.predator],
              [animal.y for animal in pop if
              animal.__class__ is animals.predator], 'ro', markersize = 5)
e, = plt.plot([animal.x for animal in pop_dead],[animal.y for animal in pop_dead
           ], 'o', color = 'black', markersize = 5) 

anim = animation.FuncAnimation(fig, animate, frames, interval = 1, repeat =False)
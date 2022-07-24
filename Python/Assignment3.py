# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:45:09 2022

@author: tcran
"""

import numpy as np 
import scipy as ip
import sympy as sy

#define matrices 
A = np.matrix([[1,2],[3,4]])
x = np.matrix([[5],[8]])

A_inverse = np.linalg.inv(A) #inverse of A

B = np.linalg.solve(A, x) # solving linear system in form Ax = B

#print(B)




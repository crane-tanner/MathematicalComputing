# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:06:47 2022

@author: tcran
"""

import sympy as sp
import numpy as np
sp.init_printing()
x,y,a,b,c = sp.symbols('x,y,b,c,a')

display(sp.solve(a*x**2 + b * x +c),)
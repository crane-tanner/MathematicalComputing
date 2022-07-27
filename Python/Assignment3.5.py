# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:25:57 2022

@author: HP
"""

import sympy as sy
sy.init_printing()

x = sy.symbols('x')
x1 = x**3 - (sy.cos(sy.pi*x)**2/(2*x**2+1))+(11/3)*(x**2)-1
display(x1)

#display the derivative
display(sy.diff(x1))
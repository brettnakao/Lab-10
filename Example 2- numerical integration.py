#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:39:42 2024

@author: brettnakao
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Integrate function f(x) from 0 to 2
def f(x): return x**2           # Define function
integral, _ = quad(f, 0, 2)     # Integrate function
integral_check = 2**3/3         # Compare to exact value of integration

# Evaluate integral g(x) from 0 to 5
def g(x): return np.exp((-x**2)/2)          # Define function
upper_limit = np.linspace(0, 5, 20)         # Define upper limit
exp_integral = np.zeros(upper_limit.size)   # Create array for integral values
for i in range(upper_limit.size):
    exp_integral[i], _ = quad(g, 0, upper_limit[i])
# Plot the results
plt.figure()
plt.plot(upper_limit, exp_integral)
plt.xlabel('x')
plt.ylabel('integral')
plt.title('Integral of g(x)')

# Evaluate infinite limits
integral_inf, _ = quad(g, -np.inf, np.inf)
integral_inf_check = np.sqrt(2*np.pi)       # Compare to exact value of integration
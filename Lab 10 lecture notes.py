#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:35:40 2024

@author: brettnakao
"""

# Exercise
from scipy.optimize import fsolve
def f(x): return x**2 - 1
print(fsolve(f, .5))
print(fsolve(f, -.5))
print(fsolve(f, [-.5, .5]))

# Numerical error
import numpy as np
def f(x): return np.sin(x)**10
print(fsolve(np.sin, 1))
print(fsolve(f, 1))

# Complex roots of polynomials
def f(x): return x * (1 + x ** 3) - 1
print(fsolve(f, 1))
print(fsolve(f, -1))

# Function with a singularity
def f(x): return 1/(x-1)
print(fsolve(f, 2, full_output=True))

# Coefficients of the polynomial x^4 + x - 1
coefficients = [1, 0, 0, 1, -1]

# Find the roots
roots = np.roots(coefficients)

print("Complex roots:", roots)
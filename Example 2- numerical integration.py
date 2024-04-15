#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:39:42 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Integrate function from 0 to 2
def f(x): return x**2
integral, _ = quad(f, 0, 2)
integral_check = 2**3/3

# Evaluate integral from 0 to 5
def g(x): return np.exp((-x**2)/2)
integral_2, _ = quad(g, 0, 5)
# Plot the results
plt.figure()
plt.plot(integral_2)

# Evaluate infinite limits
integral_inf, _ = quad(g, -np.inf, np.inf)
integral_inf_check = np.sqrt(2*np.pi)
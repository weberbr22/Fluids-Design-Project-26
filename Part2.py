#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:02:05 2026

@author: rexwb
"""

import numpy as np 
import matplotlib.pyplot as plt

Fd_C = 836762.55
Fm_C = 568954.33


theta = np.linspace(0,45,46)
theta_rad = np.radians(theta)
x1 = 0
x2 = 30* np.sin(theta_rad)
x3 = np.cos(theta_rad)*(30*np.tan(theta_rad)+30)
x4 = 30/(np.cos(theta_rad))

a = 6 
omega = (2*np.pi)/10
k = 0.0429 




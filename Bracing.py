#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:28:28 2026

@author: rexwb
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
# YZ Plane - perpendicular to flow
print('Values for the YZ Plane - perpendicular to flow')

a = 6
T = 10
omega = (2*np.pi) / T
k = 0.043
d = 40
D = 1
sin = 42/51.6
cos = 30/51.6
tan = 42/30
Cd = 1.2
Cm = 0.8
rho = 1025

# KC number - Horizontal

u_max = a * omega * ((np.cosh(k*d)) / (np.sinh(k*d)))

KC = (u_max * T) / D

print(f'Horizontal KC Value is {KC}')

# Calculate Fd induced by horizontal waves

z = np.linspace(-35, a, 100)
f = (np.cosh(k*(z + d)))**2

Id = np.trapz(f, z)

Fd = Cd * 1/2 * rho * D * (a**2 * omega**2) / (np.sinh(k*d))**2 * 1/sin * Id / 1000

print(f'Horizontal Wave Induced Fd = {Fd} kN')

# KC number - Vertical

w_max = a*omega

KC = (w_max * T) / D

print(f'\nVertical KC Value is {KC}')

# Calculate Fd induced by vertical waves

f = (np.sinh(k*(z + d)))**2

Id = np.trapz(f, z)

Fd = Cd * 1/2 * rho * D * (a**2 * omega**2) / (np.sinh(k*d))**2 * cos * Id / 1000

print(f'Vertical Wave Induced Fd = {Fd} kN') # should be 33

#%%
# XZ Plane - parallel to flow
print('\nValues for the XZ Plane - parallel to flow')

# Calculate horizontal Fd induced by horizontal waves

x = (35 + z) / tan

f = np.cosh(k*(z+d))**2 * np.sin(-k*x)**2

Id_hh = np.trapz(f, z)

Fd_hh = Cd * 1/2 * rho * D * (a**2 * omega**2) / (np.sinh(k*d))**2 * 1 / sin * Id_hh / 1000

print(f'Horizontal Fd = {Fd_hh} kN')

# Calculate vertical Fd induced by vertical waves

f = np.sinh(k*(z+d))**2 * np.cos(-k*x)

Id_hv = np.trapz(f, z)

Fd_hv = Cd * 1/2 * rho * D * (a**2 * omega**2) / (np.sinh(k*d))**2 * sin * Id_hv / 1000

print(f'Vertical Fd = {Fd_hv} kN') # Should be 64
















































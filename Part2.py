# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:37:23 2026

@author: pearc
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:56:56 2026

@author: pearc
"""

import numpy as np 
import matplotlib.pyplot as plt

theta = np.linspace(0, 45, 46)
theta_rad = np.radians(theta)
x1 = 0
x2 = 30 * np.sin(theta_rad)
x3 = np.cos(theta_rad) * (30 * np.tan(theta_rad) + 30)
x4 = 30 / (np.cos(theta_rad))

a = 6 
omega = (2 * np.pi) / 10
k = 0.0429 
T = 10
tVals = np.linspace(0, T, 100)
Cd = 1.2 
Cm = 0.8 
d = 40 
D = 4
rho = 1025

Fd_C1 = np.zeros((len(theta_rad), len(tVals)))
Fd_C2 = np.zeros((len(theta_rad), len(tVals)))
Fd_C3 = np.zeros((len(theta_rad), len(tVals)))
Fd_C4 = np.zeros((len(theta_rad), len(tVals)))

Fm_C1 = np.zeros((len(theta_rad), len(tVals)))
Fm_C2 = np.zeros((len(theta_rad), len(tVals)))
Fm_C3 = np.zeros((len(theta_rad), len(tVals)))
Fm_C4 = np.zeros((len(theta_rad), len(tVals)))

drag_C1 = np.zeros((len(theta_rad), len(tVals)))
drag_C2 = np.zeros((len(theta_rad), len(tVals)))
drag_C3 = np.zeros((len(theta_rad), len(tVals)))
drag_C4 = np.zeros((len(theta_rad), len(tVals)))

Inert_C1 = np.zeros((len(theta_rad), len(tVals)))
Inert_C2 = np.zeros((len(theta_rad), len(tVals)))
Inert_C3 = np.zeros((len(theta_rad), len(tVals)))
Inert_C4 = np.zeros((len(theta_rad), len(tVals)))

for i in range(len(theta_rad)):
    x1_i = 0
    x2_i = x2[i]
    x3_i = x3[i]
    x4_i = x4[i]
    
    for j in range(len(tVals)):
        ti = tVals[j]
        n1 = a*np.sin(omega*ti-k*x1_i)
        n2 = a*np.sin(omega*ti-k*x2_i)
        n3 = a*np.sin(omega*ti-k*x3_i)
        n4 = a*np.sin(omega*ti-k*x4_i)
        

        term_drag = (0.5 * Cd * rho * D * (a**2) * (omega**2)) / (np.sinh(k*d)**2)
        
        Fd_C1[i,j] = term_drag * (((n1 + d) / 2) + (np.sinh(2 * k * (n1 + d)) / (4 * k)))
        Fd_C2[i,j] = term_drag * (((n2 + d) / 2) + (np.sinh(2 * k * (n2 + d)) / (4 * k)))
        Fd_C3[i,j] = term_drag * (((n3 + d) / 2) + (np.sinh(2 * k * (n3 + d)) / (4 * k)))
        Fd_C4[i,j] = term_drag * (((n4 + d) / 2) + (np.sinh(2 * k * (n4 + d)) / (4 * k)))
        

        term_inert = (Cm * rho * np.pi * (D**2) * a * (omega**2)) / (4 * np.sinh(k*d))
        
        Fm_C1[i,j] = term_inert * (np.sinh(k*(n1+d)) / k)
        Fm_C2[i,j] = term_inert * (np.sinh(k*(n2+d)) / k)
        Fm_C3[i,j] = term_inert * (np.sinh(k*(n3+d)) / k)
        Fm_C4[i,j] = term_inert * (np.sinh(k*(n4+d)) / k)
 
        drag_C1[i,j] = Fd_C1[i,j] * (np.sin(omega*ti - k*x1_i))* np.abs((np.sin(omega*ti - k*x1_i)))
        drag_C2[i,j] = Fd_C2[i,j] * (np.sin(omega*ti - k*x2_i))* np.abs((np.sin(omega*ti - k*x2_i)))
        drag_C3[i,j] = Fd_C3[i,j] * (np.sin(omega*ti - k*x3_i))* np.abs((np.sin(omega*ti - k*x3_i)))
        drag_C4[i,j] = Fd_C4[i,j] * (np.sin(omega*ti - k*x4_i))* np.abs((np.sin(omega*ti - k*x4_i)))

        Inert_C1[i,j] = Fm_C1[i,j] * (np.cos(omega*ti - k*x1_i))
        Inert_C2[i,j] = Fm_C2[i,j] * (np.cos(omega*ti - k*x2_i))
        Inert_C3[i,j] = Fm_C3[i,j] * (np.cos(omega*ti - k*x3_i))
        Inert_C4[i,j] = Fm_C4[i,j] * (np.cos(omega*ti - k*x4_i))

# Totals
total_C1 = drag_C1 + Inert_C1
total_C2 = drag_C2 + Inert_C2
total_C3 = drag_C3 + Inert_C3
total_C4 = drag_C4 + Inert_C4

#gimpy



# Print correct targets!
print(f"Max Drag C1: {np.max(drag_C1):.2f}")
print(f"Max Inertia C1: {np.max(Inert_C1):.2f}")
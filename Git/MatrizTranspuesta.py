# -*- coding: utf-8 -*-
""" Definir una matriz y su transpuesta 
"""

import numpy as np

C = np.matrix("1 1 1 1; 1 2 3 4; 0 1 2 3; 0 0 1 2; 0 0 0 1")
T = np.matrix("1 ; 2; 3; 4; 5")

print(C) 
print(T)

print(C.T)
print("T^t = \n", T.T)

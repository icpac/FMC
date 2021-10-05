# -*- coding: utf-8 -*-
""" Por inspección encontrar la matriz inversa de una 
matriz elemental
"""

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np

def PrintMul(a, b):
    print("Matriz:\n", a) 
    print("Producto: \n", np.matmul(a, b))


a = np.array(
    [
        [0, 1],
        [1, 0]
    ]
)

b = np.array(
    [
        [1, 0],
        [5, 1]
    ]
)

binv = np.array(
    [
        [1, 0],
        [-5, 1]
    ]
)

c = np.array(
    [
        [1, 0, 0],
        [0, 1, -3],
        [0, 0, 1]
    ]
)

cinv = np.array(
    [
        [1, 0, 0],
        [0, 1, 3],
        [0, 0, 1]
    ]
)

PrintMul(a, a)
PrintMul(b, binv)
PrintMul(c, cinv)
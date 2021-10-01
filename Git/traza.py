__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"


import numpy as np

""" La matriz de prueba """
A = np.array(
    [
        [1, 2, -1],
        [2, 1, 3],
    ]
)

B = np.array(
    [
        [5, 4],
        [6, 5],
        [1, 0]
    ]
)

""" Multiplicación y traza """
AB = np.matmul(A, B)
print(np.matrix.trace(AB))

BA = np.matmul(B, A)
print(np.matrix.trace(BA))

B = np.array(
    [
        [2, 0],
        [0, 2],
    ]
)
print(np.matmul(B,B)) 

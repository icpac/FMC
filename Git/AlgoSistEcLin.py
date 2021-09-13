import numpy as np


def Gauss(A):
    n = A.shape[0]

    for j in range(0, n):
        if A[j][j] == 0: 
            print("La matriz no es Regular ")
            return None
        else:
            for i in range(j+1, n):
                lij = A[i,j]/A[j,j]
                A[i] = A[i] - lij * A[j]

    return A


def suma(A, x, i):
    sum = 0
    n = A.shape[0]
    #for j in range(0, i+1):
    for j in range(n-1, i, -1):
        sum += A[i][j]*x[j]
    return sum

def Sustitucion(A):
    n = A.shape[0]
    x = np.zeros(n)
    x[n-1] = A[n-1,n]/ A[n-1, n-1]
    
    for i in range ((n-1)-1, 0-1, -1):
        x[i] = 1/ A[i][i] * (A[i, n] - suma(A, x, i)) 
    return x

A = np.array(
    [
        [1, 2, 1, 2],
        [2, 6, 1, 7],
        [1, 1, 4, 3]
    ], dtype='f'
)

"""
a = np.array([
    [1, 1, 3, -2, -1], 
    [5, -2, 3, 7, 8],
    [-3, -1, 2, 7, 5],
    [5, 3, 1, -2, -7]], dtype='f')"""

"""
a = np.array([
    [1, 1,1, 1, 0], 
    [1, 2, 3, 4, 0],
    [1, 3, 6, 10, 0],
    [1, 4, 10, 20, 0]], dtype='f')"""

"""
a = np.array([
    [2, -1, -1, 0], 
    [3, 4, -2, 0],
    [3, -2, 4, 0]], dtype='f')"""

a = np.array([
    [1, -1, 1, 1, 2, -1], 
    [-1, 1, 1, 1, -4, 3],
    [-1, -1, 1, 1, -2, 3],
    [1, -2, 1, 2, 3, -1],
    [0, -4, 1, 5, 3, 1]
    ], dtype='f')

a = np.array([
    [1, 2, 3, 4], 
    [-1, 3, 0, 1],
    [-5, 6, 7, 0]
    ], dtype='f')


print("Matriz: \n", a)
Gaus= Gauss(a)
if Gaus.all() != None:
    print("Matriz: \n", np.round(Gaus, 3))
    Sol = Sustitucion(Gaus)
    print("Solucion:\n", np.round(Sol, 3))

    B = np.delete(a, -1, axis=1)
    Sol = np.array(Sol).reshape(3, 1)
    print("Solucion: \n", Sol)
    print("B:\n", B)
    print("Solución: \n", np.round(np.matmul(B, Sol), 2)) 
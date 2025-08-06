""" Funciones universales parte II
    NumPy.SQRT(array)   Raiz cuadrada"""

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print('Matriz A -->', a)
print('Matriz B -->', b)

raiz_A  = np.sqrt(a)
raiz_B = np.sqrt(b)

print('\nLa raiz cuadrada de la matriz A es \n', raiz_A)
print('\nLa raiz cuadrada de la matriz B es \n', raiz_B)

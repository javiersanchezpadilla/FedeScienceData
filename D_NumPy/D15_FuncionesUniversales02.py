""" Funciones universales parte II
    NumPy.EXP(array)    Exponencial de un array"""

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print('Matriz A -->', a)
print('Matriz B -->', b)

exponencial = np.exp(a)
print('\nEl exponencial de la matriz A es \n', exponencial)

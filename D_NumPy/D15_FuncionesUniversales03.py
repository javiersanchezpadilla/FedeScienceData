""" Funciones universales parte II
    NumPy.LOG(array)    Calculo del logaritmo natural"""

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print('Matriz A -->', a)
print('Matriz B -->', b)

logaritmoA = np.log(a)
logaritmoB = np.log(b)

print('\nEl Logaritmo natural de la matriz A es \n', logaritmoA)
print('\nEl Logaritmo natural de la matriz B es \n', logaritmoB)

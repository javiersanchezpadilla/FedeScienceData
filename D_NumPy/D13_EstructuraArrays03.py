""" Estudiaremos la estructura de los arrays en Python
    Transposicion de matrices"""

import numpy as np 

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

array_mod = array.reshape(-1, 3)

print('Valores originales: \n', array_mod)
# TRansposicion de valores en la matriz
array_volteado = array_mod.transpose()
print('\nEl arreglo transpuesto es: \n', array_volteado)

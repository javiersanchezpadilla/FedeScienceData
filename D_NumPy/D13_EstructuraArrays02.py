""" Estudiaremos la estructura de los arrays en Python"""

import numpy as np 

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

array_modif = array.reshape(3, 3)

# podemos hacer que numpy calcule la proporcion de filas
array_mod2 = array.reshape(-1, 3)
print('\nreshape con -1 para que numpy calcule las filas')
print(array_mod2)

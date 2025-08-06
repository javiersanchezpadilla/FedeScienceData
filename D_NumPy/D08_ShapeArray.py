""" Conociendo la forma de los arrays.
    Usaremos SHAPE para conocer la forma"""

import numpy as np 

a = [[1, 2], 
     [3, 4]]

b = [[5, 6], 
     [7, 8]]


# Concatenado por filas AXIS=0
concatenado_axis_0 = np.concatenate([a, b], axis=0)
print('Concatenado con AXIS=0')
print(concatenado_axis_0)
print('Shape de AXIS=0', concatenado_axis_0.shape)

# Concatenado por columnas AXIS=1
concatenado_axis_1 = np.concatenate([a, b], axis=1)
print('\nConcatenado con AXIS=1')
print(concatenado_axis_1)
print('Shape de AXIS=1', concatenado_axis_1.shape)

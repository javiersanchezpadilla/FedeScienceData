""" Operaciones de concatenacion mediante
    el uso del argumento AXIS,
    AXIS = 0
    AXIS = 1 

    Concatenar arrays de una dimensaion"""

import numpy as np 


array1 = np.array([1, 2, 3])
print(f'Array 1 {array1}')

array2 = np.array([4, 5, 6])
print(f'Array 2 {array2}')

# Concatenamos por axis=0 (es la unica opcion para 1D)
array_concatenado_1D = np.concatenate((array1, array2), axis=0)
print(f'Array de una Dimension concatenado \n {array_concatenado_1D}')

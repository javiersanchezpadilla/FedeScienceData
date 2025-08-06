""" Estudiaremos la estructura de los arrays en Python
    Cambiar arreglos de dos dimensiones en arreglos 
    de una sola dimension."""

import numpy as np 

array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

array_modif_reshape = array.reshape(1, 9)
array_modif_flatten = array.flatten()
array_modif_ravel = array.ravel()

print('\nARREGLO ORIGINAL\n', array)
print('\nCAMBIO DE ARREGLOS DE DOS DIMENSIONES A UNA DIMENSIÓN:')

print('\nMediante RESHAPE:', array_modif_reshape)
print('Mediante FLATTEN:', array_modif_flatten)
print('Mediante RAVEL  :', array_modif_ravel)


""" Uso de funciones avanzadas y universales.
    Broadcast permite hacer operaciones entre
    arrays de distintos tamaños multiplicacion"""

import numpy as np 

array1 = np.array([1, 2, 3])
print('Array 1: ', array1)

array2 = np.array([[0], [10], [20], [30]])
print('\nArray 2:\n', array2)

# USO DE BROADCAST  Se suma lo que hay en la fila mas la columna
broadcast_suma = array1 * array2
print('\nSuma de los arrays:\n', broadcast_suma)

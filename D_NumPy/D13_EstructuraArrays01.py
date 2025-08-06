""" Estudiaremos la estructura de los arrays en Python
    Moficando la dimension de un array con el uso de

    Arreglo.RESHAPE(Filas, Columnas)
    
"""

import numpy as np 

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print('El array tiene la forma: ', array)
print('Obtenemos la forma del array: ', array.shape)
print('\nCambiando la dimension del arreglo')
array_modif = array.reshape(3, 3)
print(array_modif)


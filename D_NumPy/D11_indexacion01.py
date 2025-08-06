""" En esto programas aprendere como indexar los
    arrays, para controlar e incluso hacer slicing
"""

import numpy as np 

array1d = np.array([1, 2, 3, 4, 5])
array2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Acceder a elementos especificos dentro de un array
# esto tal como se hace en la listas mediante indices

print('\nAccediendo a los elementos del array una dimension')
print(array1d)
print('\nElemento 1 pos[0]', array1d[0])
print('Elemento 2 pos[1]', array1d[1])
print('Elemento 3 pos[2]', array1d[2])
print('Elemento 4 pos[3]', array1d[3])
print('Elemento 5 pos[4]', array1d[4])

print('\nAccediento a los elemnentos del array 2 Dimensiones')
print(array2d)
print('\nElemento 1 pos[0]', array2d[0])    # fila 1
print('Elemento 2 pos[1]', array2d[1])      # fila 2
print('Elemento 3 pos[2]', array2d[2])      # fila 3

print('\nAccediendo a los elementos individuales del array 2D')
print('\nfila 1 elemento[0]   ', array2d[0])
print('fila 1 Elemento 1 [0] ', array2d[0][0])
print('fila 1 Elemento 2 [1]   ', array2d[0][1])
print('fila 1 Elemento 3 [2]     ', array2d[0][2])

print('\nOtra forma de acceder a los elemnentos individuales')
print('\nfila 2 elemento[1]   ', array2d[1])
print('fila 2 Elemento 1 [0] ', array2d[1, 0])
print('fila 2 Elemento 2 [1]   ', array2d[1, 1])
print('fila 2 Elemento 3 [2]     ', array2d[1, 2])

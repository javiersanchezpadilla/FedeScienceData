""" Crea un array bidimensional al que nombres: 
    matriz con forma (3, 3) que representa una matriz 
    de números del 1 al 9. 
    Escribe un código para extraer la segunda fila 
    completa de esta matriz. Almacenala en una variable 
    nombrada segunda_fila"""

import numpy as np 

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

segunda_fila = matriz[1]

print('La matriz completa es:\n', matriz)
print('\nLa segunda fila es :',  segunda_fila)



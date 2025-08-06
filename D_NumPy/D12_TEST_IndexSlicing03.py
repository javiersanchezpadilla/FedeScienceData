""" Crea un array bidimensional al que nombres: matriz con forma 
    (3, 3) que representa una matriz de números del 1 al 9.
    Luego utiliza la indexacion booleana para guardar en una 
    variable llamada pares_impares los numeros pares como true, 
    y los impares como false."""

import numpy as np 

matriz = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

pares_impares = matriz % 2 == 0

print('La matriz original es:\n', matriz)
print('\nLa matriz de valores impares es:\n', pares_impares)

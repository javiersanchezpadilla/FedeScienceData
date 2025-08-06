""" Crea un programa que defina dos arrays usando NumPy: 
    el primer array A debe ser un array unidimensional 
    de 5 elementos, iniciando en 1 y con pasos de 2 
    (i.e., [1, 3, 5, 7, 9]), y el segundo array B debe 
    ser un array bidimensional de forma (5,1), con 
    valores que comiencen en 10 y aumenten de 10 en 10 
    (i.e., [[10], [20], [30], [40], [50]]).

    Utiliza el concepto de broadcasting para sumar estos 
    dos arrays y almacena su resultado en una variable 
    llamada resultado
"""

import numpy as np 

A = np.array([1, 3, 5, 7, 9])
B = np.array([[10], [20], [30], [40], [50]])

resultado = A + B
 
print('Matriz A:', A)
print('\nMatriz B:\n', B)
print('\nBroadcasting Suma de A + B\n', resultado)

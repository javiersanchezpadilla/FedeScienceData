""" Crea un programa que defina dos arrays usando NumPy: 
    el primer array A debe ser un array unidimensional de 
    10 elementos, iniciando en 1 hasta el 10, y el segundo 
    array B debe ser un array bidimensional de forma (5,1), 
    con valores que comiencen en 10 y aumenten de 10 en 10 
    (i.e., [[10], [20], [30], [40], [50]]).

    Utiliza el concepto de broadcasting para multiplicar 
    estos dos arrays almacena el resultado en una variable 
    llamada resultado."""

import numpy as np 

A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = np.array([[10], [20], [30], [40], [50]])

resultado = A * B

print('Matriz A:', A)
print('\nMatriz B:\n', B)
print('\nBroadcasting Producto de A * B\n', resultado)

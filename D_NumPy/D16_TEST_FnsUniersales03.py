""" Crea un programa que defina un array usando NumPy: 
    A debe ser un array unidimensional de solamente 3 
    elementos, iniciando en 1 y terminando en 3 (inclusive)

    Utiliza la función matemática adecuada para almacenar 
    en una variable llamada resultado el exponente de cada 
    numero contenido en A."""

import numpy as np 

A = np.array([1, 2, 3])

resultado = np.exp(A)

print('Valor de la matriz -->:', A)
print('\nValor de la matriz exponencial:\n', resultado)

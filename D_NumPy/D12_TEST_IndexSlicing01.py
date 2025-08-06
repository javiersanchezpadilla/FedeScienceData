""" Crea un array de numpy nombrado numeros que contenga los 
    primeros 10 números enteros (del 1 al 10). Luego escribe 
    un código para obtener el quinto elemento de este array. 
    Almacenalo en una variable llamada quinto_elemento

    Recuerda que los elementos se cuentan a partir de 1 en 
    adelante, mientras que los indices de los elementos que 
    componen una lista o array comienzan desde 0.
"""

import numpy as np 

numeros = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
quinto_elemento = numeros[4]

print(quinto_elemento)

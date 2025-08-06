""" Crea un array bidimensional llamado: array_2d
    La primera dimensión del array debe contener los 
    números 1 2 3
    La segunda dimensión del array debe contener los 
    números 4 5 6
    Crea una variable llamada: largo_array_2d   
    donde almacenes el largo del array creado anteriormente.
"""

import numpy as np 

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
largo_array_2d = len(array_2d)
print(array_2d)
print(largo_array_2d)

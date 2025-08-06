
""" Crea un array unidimensional array_original con 
    los números del 1 al 6, utiliza el método correcto 
    para transformarlo en un array bidimensional de 2 
    filas y 3 columnas. Almacena el resultado en una 
    variable llamada array_reshaped"""

import numpy as np 

array_original = np.array([1, 2, 3, 4, 5, 6])
array_reshaped = array_original.reshape(2, 3)

print('Array original\n', array_original)
print('Array modificado a dos dimensiones\n', array_reshaped)

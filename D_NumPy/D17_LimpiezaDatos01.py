""" Limpieza de datos.
    El tipo de dato NaN Not a Number"""

import numpy as np 

arreglo = np.array([1, 2, np.nan, 4, 5])
print(arreglo)

# podemos crear un arreglo boleano para establecer una condicion
print(np.isnan(arreglo))

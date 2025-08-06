""" Crea dos arrays unidimensionales, array1 y array2, 
    donde array1 contiene los números del 1 al 5 y 
    array2 contiene los números del 6 al 10. 
    Utiliza la función de numpy adecuada para concatenar 
    array1 y array2 en un nuevo array llamado 
    array_concatenado."""

import numpy as np 

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
array_concatenado = np.concatenate([array1, array2])
print(array_concatenado)


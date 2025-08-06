""" Dado el siguiente array de numpay

        array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])

    Crea una variable nombrada sustituir_nans donde almacenes 
    los np.nan encontrados en el array sustituidos por cero (0). 
    Emplea la función correcta de NumPy para esta finalidad."""

import numpy as np 

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])

sustituir_nans = np.where(np.isnan(array), 0, array)

print('Valores del arreglo original: ', array)
print('Arreglo con ceros por NaNs:   ', sustituir_nans)

""" Dado el siguiente array de numpay

        array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])

    Utiliza la función adecuada para comprobar la presencia de NaN, 
    y almacena el resultado en una variable llamada: nan_presencia
"""

import numpy as np 

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
nan_presencia = np.isnan(array)

print('Valor del array original', array)
print('Detectar valores NaN:   ', nan_presencia)

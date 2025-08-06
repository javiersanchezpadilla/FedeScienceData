""" Dado el siguiente array de numpay

        array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])

    Crea una variable llamada promedio_sin_nans que almacene el 
    promedio excluyendo cualquier valor np.nan. Debes utilizar 
    una función de NumPy que ignore los np.nan automáticamente 
    para este cálculo."""

import numpy as np 

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])

promedio_sin_nans = np.nanmean(array)

print('Valores del arreglo original:    ', array)
print('El valor promedio sin los NaN,es:', promedio_sin_nans)

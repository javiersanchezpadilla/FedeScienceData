""" Limpieza de datos.
    El tipo de dato NaN Not a Number esta presente
    por lo que si intento calcular el promedio el 
    resultado sera NaN"""

import numpy as np 

arreglo = np.array([1, 2, np.nan, 4, 5])
print(arreglo)

# podemos crear un arreglo boleano para establecer 
# una condicion
print(np.isnan(arreglo))

# Calculando el valor promedio normal
# el resultado será un NaN
print('\nPromedio (tomando todos los valores):      ', np.mean(arreglo))

# Calculando el promedio tomando los valores NaN
# pero ignorandolos. (1+2+4+5)/4 = (12/4 = 3)
print('Promedio tomando los Nan pero ignorandolos:', np.nanmean(arreglo))


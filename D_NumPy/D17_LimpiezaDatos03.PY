""" En NumPy, varias funciones están diseñadas para manejar 
    valores NaN (Not a Number) ignorándolos al realizar cálculos. 
    Estas funciones permiten realizar operaciones como sumas, 
    promedios, mínimos, máximos, etc., sin que los valores NaN afecten 
    los resultados."""

import numpy as np

# Crear un array con valores NaN
arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# Calcular la media ignorando los NaN
mean_val = np.nanmean(arr)
print(f"La media ignorando NaN es: {mean_val}")  # Salida: 3.5

# Suma de elementos ignorando NaN
sum_val = np.nansum(arr)
print(f"La suma ignorando NaN es: {sum_val}")  # Salida: 14.0

# Encontrar elementos NaN
is_nan_array = np.isnan(arr)
print(f"¿Son NaN?: {is_nan_array}") # Salida: [False False  True False  True False]

#Filtrar valores que no son NaN
arr_no_nan = arr[~np.isnan(arr)]
print(f"Array sin NaN: {arr_no_nan}") # Salida: [1. 2. 4. 6.]

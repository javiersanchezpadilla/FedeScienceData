""" Sustitución de valores mediante 
    la sentencia 
    WHERE
        'Donde se cumpla una condicion hacemos algo'
        'Donde no se cumpla una condicion hacemos otra cosa'
"""

import numpy as np 

arreglo = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8])
print('Arreglo original con valores NaN      ', arreglo)

# donde la evaluacion de la posición del arreglo sea NaN (true)
# devuelve un cero, en otro caso toma el valor original del arreglo
array_con_ceros = np.where(np.isnan(arreglo), 0, arreglo)
print('Arreglo modificando los valores NaN:  ', array_con_ceros)                       

# PAra reemplazar los valores NaN por sus valores promedio
# Primero calculamos el valor promedio del arreglo sin los NaN
promedio_sin_Nan = np.nanmean(arreglo)
print('Valor promedio calculado del arreglo  ', promedio_sin_Nan)

# Ahora cambiamos en el array los valores NaN por sus promedios
array_con_promedios = np.where(np.isnan(arreglo), promedio_sin_Nan, arreglo)
print('Arreglo con promedios en lugar de NaN:', array_con_ceros)

# Eliminando los valores NaN 
# PAra entender la logica de esta operación observemos que sucede si filtro 
# el resulado será los valores NaN, así que haremos la negación de este filtro
# para que nos de los valores del tipo not NaN
array_filtrado_losNaN = arreglo[np.isnan(arreglo)]
print('Arreglo filtrado solo los Nan         ', array_filtrado_losNaN)

array_filtrado_losNotNan = arreglo[~np.isnan(arreglo)]
print('Arreglo filtrado solo los NOT Nan     ', array_filtrado_losNotNan)

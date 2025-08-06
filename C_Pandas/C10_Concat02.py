""" CONCATENAR DATA FRAMES DE FORMA HORIZONTAL:
    el argumento AXIS cambia, por defecto AXIS=0 (eje 'y'),
    pero podemos cambiarlo a AXIS=1 (eje 'x')

    valores para la contatenacion 
        axis=0 concatena de forma vertical por columna
        axis=1 concatena de forma horizontal por filas
"""

import pandas as pd 

df1 = pd.DataFrame({'Nombre': ['Juan', 'Gabriela', 'Elena'],
                    'Edad': [23, 31, 21]})

df2 = pd.DataFrame({'Nombre': ['Carmela', 'Max', 'Leticia'],
                    'Edad': [34, 25, 29]})

print('Datos del primer data frame')
print(df1)
print('\nDatos del segundo data frame')
print(df2)

print('\nConcatenación de ambos data frames')

df_concatenado = pd.concat([df1, df2], axis=1)
print(df_concatenado)

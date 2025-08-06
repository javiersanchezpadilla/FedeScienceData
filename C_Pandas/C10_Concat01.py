""" Concatenar data frames mediante concat (CONCAT BASICO)
    Imaginemos que todos los dias no reportan una tabla de ventas
    estas ventas tienen que agregarse día a día, claro partimos
    de que son el mismo tipo de tablas con las mismas columnas, 
    esto es, con la misma estructura.
    CONCAT nos va a permnitir juntar esas tablas para solo manejar
    una sola
    
    pandas.concat( [ df1, df2])

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
df_concatenado = pd.concat([df1, df2])
print(df_concatenado)

""" AGREGANDO ETIQUETAS.
    De esta manera podemos identificar a que grupo de datos
    pertenecen los valores concatenados.
    Las etiquetas pueden ser cualquier valor, solo son para
    asocial los grupos de valores"""

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
df_concatenado = pd.concat([df1, df2], keys=['df1', 'df2'])
print(df_concatenado)
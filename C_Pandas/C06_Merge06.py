""" variable = pandas.merge (df1, df2, left_index=True, right_index=True)

    En este tipo de union de los data frame se agregan los índices originales
    de cada uno de los data frame, pero ademas la union de las tablas toma
    como serieDeRelacion el índice de ambos data frame
"""

import pandas as pd 

df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Ana', 'Luis', 'Carlos']})

df2 = pd.DataFrame({'ID':[1, 2, 4],
                    'Edad': [25, 30, 22]})

print('Data frame 1')
print(df1)
print('\nData frame 2')
print(df2)

print('\nData frame combinado')
# df_combinado = pd.merge(df1, df2, on='ID', how='right')
df_combinado = pd.merge(df1, df2, left_index=True, right_index=True)
print(df_combinado)

""" Uso de merge con dos data frame
    Elegir que unir de los data frames  

    variable = pandas.merge (df1, df2, on='serieUnion', how='outer')

    Cuando usamos HOW por con el valor OUTER, incluye todos los 
    valores de ambas tablas y aquellos valores que no tengan relación
    los rellena con valores Nan Nt a number, que indica que falta valor
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
df_combinado = pd.merge(df1, df2, on='ID', how='outer')
print(df_combinado)

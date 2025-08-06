""" Uniendo tablas JOIN definiendo HOW='OUTER' """

import pandas as pd 

df1 = pd.DataFrame({'Salario': [30000, 45000, 30000],
                    'Antiguedad': [9, 13, 12],},
                     index = [1, 2, 3])

df2 = pd.DataFrame({'Ciudad': ['Iguala', 'Acapulco', 'Chilpancingo' ],
                    'Jerarquía': ['Baja', 'Alta', 'Media']},
                    index = [1, 2, 4])

print('Datos del data frame 1')
print(df1)
print('\nDatos del data frame 2')
print(df2)

print('\nDatos del data frame unido')
df_unido = df1.join(df2, how='outer')
print(df_unido)
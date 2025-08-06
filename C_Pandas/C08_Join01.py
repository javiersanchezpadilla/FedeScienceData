""" Fusionado de data frames con join
    Bajo el concepto de MERGE fusionabamos dos data frame mediante
    una columna en particular.
    Bajo el concepto de JOIN se realiza una union mendiante su indice
    o de una columna clave, pero no de una columna compartida, solo
    confiando en que sus índices se corresponden entre si
    En el ejemplo mostrado las DF no tienen una columna comun
    por fececto HOW='LEFT' aunque no se declare
"""

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
df_unido = df1.join(df2)
print(df_unido)

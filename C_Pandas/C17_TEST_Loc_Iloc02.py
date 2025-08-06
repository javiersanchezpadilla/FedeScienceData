""" Utiliza loc para seleccionar las filas "fila1" y "fila3" del 
    DataFrame df. Tu resultado debe ser un DataFrame nombrado resultado.

            df = pd.DataFrame({
                'Nombre': ['Ana', 'Luis', 'Carmen'],
                'Edad': [25, 30, 22],
                'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
            }, index=['fila1', 'fila2', 'fila3'])
"""

import pandas as pd 

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carmen'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}, index=['fila1', 'fila2', 'fila3'])

print(df)

resultado = df.loc[[True, False, True]]
print(resultado)

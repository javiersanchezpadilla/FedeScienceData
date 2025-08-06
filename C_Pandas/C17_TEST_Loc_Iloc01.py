""" Utiliza loc para seleccionar los datos de la fila denominada "fila2" 
    en el siguiente DataFrame df.  Tu resultado debe ser una Serie de 
    Pandas llamada resultado

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
resultado = df.loc['fila2']
print(resultado)

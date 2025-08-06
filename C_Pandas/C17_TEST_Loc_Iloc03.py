""" Utiliza iloc para seleccionar las primeras dos filas y las últimas dos 
    columnas del siguiente DataFrame df. El resultado debe ser un DataFrame 
    llamado resultado

            df = pd.DataFrame({
                'A': [1, 2, 3, 4],
                'B': [5, 6, 7, 8],
                'C': [9, 10, 11, 12],
                'D': [13, 14, 15, 16]
            })
"""

import pandas as pd 

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
})

print(df)

# Toma de las posiciones de indices 0, (2-1)=1 y 
# toma las do súltimas columnas
resultado = df.iloc[:2, -2:]
print(resultado)

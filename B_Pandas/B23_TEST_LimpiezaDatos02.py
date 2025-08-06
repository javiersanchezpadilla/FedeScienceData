""" El conjunto de datos proporcionado tiene algunas entradas duplicadas.

    data = {
        'ID': [1, 2, 3, 4, 1],
        'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
        'Cantidad': [10, 20, 30, 40, 50],
        'Precio': [100, 200, 300, 400, 100]
    }
Escribe un script en Python usando Pandas para eliminar las filas duplicadas en el conjunto de datos. Almacena el resultado en una variable llamada: df_sin_duplicados
"""

import pandas as pd 


data = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]
}

df = pd.DataFrame(data)
df_uniccos = df.drop_duplicates(subset='Producto')
print('TABLA ORIGINAL\n', df)
print('TABLA REDUCIDA\n', df_uniccos)

""" Dada una tabla (Diccionario) de ventas que contiene información sobre productos vendidos, 
    incluyendo ID, Producto, Cantidad y Precio,

    data = {
        'ID': [1, 2, 3, 4, 5],
        'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
        'Cantidad': [10, 20, 30, None, 50],
        'Precio': [100, 200, 300, 400, None]
    }

    Escribe un código en Python usando Pandas para contar los valores nulos por columnas.
"""


import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
    'Cantidad': [10, 20, 30, None, 50],
    'Precio': [100, 200, 300, 400, None]
}

df = pd.DataFrame(data)
print(df.isnull().sum())

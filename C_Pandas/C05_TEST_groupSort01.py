""" Crea un DataFrame a partir del siguiente diccionario de datos de películas.

    datos = {
        'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
        'año': [2001, 2000, 2005, 2010],
        'rating': [7.2, 6.5, 8.1, 7.5]
    }
    Luego, ordena este DataFrame por la columna 'año' en orden ascendente. 
    Asegurate de almacenar el diccionario ordenado en una variable llamada: df_ordenado
"""

import pandas as pd 

datos = {
        'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
        'año': [2001, 2000, 2005, 2010],
        'rating': [7.2, 6.5, 8.1, 7.5]
    }

df = pd.DataFrame(datos)
df_ordenado = df.sort_values(by='año', ascending=True)
print(df_ordenado)


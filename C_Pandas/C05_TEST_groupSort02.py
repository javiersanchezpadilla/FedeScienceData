""" Usando el mismo DataFrame del Ejercicio anterior.

    datos = {
        'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
        'año': [2001, 2000, 2005, 2010],
        'rating': [7.2, 6.5, 8.1, 7.5]
    }
    Ordena las películas primero por 'rating' en orden descendente y luego 
    por 'año' en orden ascendente. Asegurate de almacenar el dataframe 
    ordenado en una variable llamada: df_ordenado
"""
import pandas as pd 

datos = {
        'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
        'año': [2001, 2000, 2005, 2010],
        'rating': [7.2, 6.5, 8.1, 7.5]
    }

df = pd.DataFrame(datos)
df_ordenado = df.sort_values(by=['rating','año'], ascending=[False, True])
print(df_ordenado)


""" Crea un nuevo DataFrame a partir del siguiente diccionario que contiene datos 
    de películas incluyendo su género.

    datos = {
        'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E'],
        'género': ['Acción', 'Drama', 'Acción', 'Comedia', 'Drama'],
        'rating': [7.2, 8.5, 9.1, 6.5, 7.8]
    }

    Luego, agrupa las películas por 'género' y calcula el promedio de 'rating' 
    para cada género.  
    Asegurate de almacenar el grupo y promedio en una variable llamada: 
    promedio_rating_por_genero
"""
import pandas as pd 

datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E'],
    'género': ['Acción', 'Drama', 'Acción', 'Comedia', 'Drama'],
    'rating': [7.2, 8.5, 9.1, 6.5, 7.8]
}

df = pd.DataFrame(datos)
promedio_rating_por_genero = df.groupby('género')['rating'].mean()
print(promedio_rating_por_genero)



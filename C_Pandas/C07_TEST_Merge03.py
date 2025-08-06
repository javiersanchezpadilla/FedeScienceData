""" Dispones de dos DataFrames, productos y reviews, que contienen información sobre 
    productos y las reseñas asociadas a estos productos, respectivamente. 
    Los Data Frames se presentan de la siguiente manera:

    productos = pd.DataFrame({
        'ID': [10, 11, 12],
        'Nombre': ['Teclado', 'Mouse', 'Monitor'],
        'Marca': ['Logitech', 'Razer', 'Dell']
    })
    
    reviews = pd.DataFrame({
        'ID': [10, 11, 12],
        'Calificación': [5, 4, 4],
        'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
    })

    Tu tarea consiste en fusionar productos con reviews para obtener un Data Frame que 
    combine la información de ambos (al cual debes nombrar: productos_reviews), manteniendo 
    los índices originales de cada uno.
    Utiliza los parámetros adecuados de la función merge() para realizar esta combinación. 
    El Data Frame resultante productos_reviews debe contener las columnas de ambos Data Frames 
    originales, permitiendo así un análisis detallado de cada producto junto con sus reseñas.
"""

import pandas as pd 

productos = pd.DataFrame({
    'ID': [10, 11, 12],
    'Nombre': ['Teclado', 'Mouse', 'Monitor'],
    'Marca': ['Logitech', 'Razer', 'Dell']
})

reviews = pd.DataFrame({
    'ID': [10, 11, 12],
    'Calificación': [5, 4, 4],
    'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
})

productos_reviews = pd.merge(productos, reviews, left_index=True, right_index=True)
print(productos_reviews)


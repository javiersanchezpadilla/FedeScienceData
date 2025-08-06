""" Dado el DataFrame productos_df con columnas ProductoID, Nombre y Precio, y el 
    DataFrame categorias_df con columnas CategoriaID y NombreCategoria

        # Creamos los DataFrames de ejemplo
        productos_df = pd.DataFrame({
            'ProductoID': [1, 2, 3, 4],
            'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
            'Precio': [100, 150, 200, 250]
        }).set_index('ProductoID')
        
        categorias_df = pd.DataFrame({
            'CategoriaID': [1, 2],
            'NombreCategoria': ['Categoría 1', 'Categoría 2']
        }).set_index('CategoriaID')

    Donde ambos DataFrames están indexados por ProductoID y CategoriaID respectivamente, 
    realiza una unión usando el método join() para combinar estos DataFrames en un nuevo 
    DataFrames  nombrado: df_combinado basándote en sus índices, asegurándote de que todos 
    los productos se muestren, independientemente de si tienen una categoría asignada o no.

    Utiliza el método adecuado  para asegurar que todos los registros del DataFrame de la 
    izquierda (productos_df en este caso) se incluyan en el DataFrame resultante df_combinado, 
    independientemente de si tienen una correspondencia en el DataFrame de la derecha (categorias_df).
"""
import pandas as pd

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')

print('Primer data frame de productos')
print(productos_df)

print('\nSegundo data frame de categorias')
print(categorias_df)

print('\nData frame resultado de la union')
df_combinado = productos_df.join(categorias_df, how='left')
print(df_combinado)


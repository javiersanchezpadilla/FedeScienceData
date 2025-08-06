"""  En este ejercicio, trabajará con dos DataFrames: productos_df y categorias_df.

        productos_df = pd.DataFrame({
            'ProductoID': [1, 2, 3, 4],
            'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
            'Precio': [100, 150, 200, 250]
        })
        
        productos_df = productos_df.set_index('ProductoID')
        
        categorias_df = pd.DataFrame({
            'CategoriaID': [1, 2, 3],
            'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
        }).set_index('CategoriaID')

    Tu tarea es combinar estos DataFrames en un DataFrame llamado df_combinado de tal manera 
    que se conserven todos los registros del DataFrame de productos_df, incluso si no tienen 
    una categoría correspondiente en categorias_df. Para esto, debes utilizar el parámetro 
    how="right" en el método join().

    Instrucciones:

    Combina los DataFrames productos_df y categorias_df utilizando el método join() y el 
    parámetro how="right".
    Asigna el resultado a un DataFrame llamado df_combinado.
"""

import pandas as pd

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})

productos_df = productos_df.set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')

print('Data frame productos')
print(productos_df)

print('\nData frane categorias')
print(categorias_df)

print('\nAmbos data frame combinados')
df_combinado = categorias_df.join(productos_df, how='right')
print(df_combinado)
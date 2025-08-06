""" Dado los siguientes DataFrames que representan las ventas de 
    dos tiendas diferentes en el mismo mes:

            tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 
                                     'Cantidad': [500, 300]})
            tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 
                                     'Cantidad': [400, 250]})

    Tu tarea es concatenar estos DataFrames verticalmente en un nuevo DataFrame 
    llamado ventas_tienda, utilizando el parámetro keys para marcar cada bloque 
    de datos con las etiquetas "Tienda A" y "Tienda B", respectivamente. 
    Asegúrate de que el DataFrame resultante tenga un índice jerárquico que 
    refleje estas claves.
"""

import pandas as pd

tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 'Cantidad': [500, 300]})
tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 'Cantidad': [400, 250]})

print('Tienda A')
print(tienda_a)
print('\nTienda B')
print(tienda_b)

print('\nTabla resultado de la union de ambas tablas')
ventas_tienda = pd.concat([tienda_a, tienda_b], 
                          keys=['Tienda A', 'Tienda B'])
print(ventas_tienda)

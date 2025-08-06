""" Tienes dos conjuntos de datos representados por los siguientes DataFrames 
    ventas_enero y ventas_febrero, que contienen las ventas de diferentes 
    productos en los meses de enero y febrero, respectivamente.

    ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                                 'Cantidad': [300, 200, 150]})
    ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                                   'Cantidad': [350, 210, 170]})

    Tu tarea es utilizar el método concat() para concatenar estos dos DataFrames 
    verticalmente en un nuevo DataFrame llamado ventas_total. 
    Asegúrate de ignorar los índices originales para que el índice del DataFrame 
    resultante sea continuo."""

import pandas as pd 

ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                             'Cantidad': [300, 200, 150]})

ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                               'Cantidad': [350, 210, 170]})

print('Ventas de Enero')
print(ventas_enero)
print('\nVentas febrero')
print(ventas_febrero)

print('\nVentas TOTAL:')
ventas_total = pd.concat([ventas_enero, ventas_febrero], 
                         ignore_index=True)
print(ventas_total)

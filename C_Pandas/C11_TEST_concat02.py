""" Considera los siguientes DataFrames datos_cliente y compras_cliente, 
    que contienen información sobre los clientes y sus compras, 
    respectivamente.

            datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"], 
                                          'Edad': [34, 45, 28]})
            compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"], 
                                            'Precio': [15.50, 0.50, 2.00]})

    Utiliza el método concat() para unir estos dos DataFrames horizontalmente, 
    formando un nuevo DataFrame llamado info_cliente. Asegúrate de que los índices se 
    mantengan para que cada fila corresponda correctamente entre los dos DataFrames.
"""
import pandas as pd

datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"], 
                              'Edad': [34, 45, 28]})

compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"], 
                                'Precio': [15.50, 0.50, 2.00]})

print('Datos del cliente')
print(datos_cliente)
print('\nCompras de los clientes')
print(compras_cliente)

print('\nInformación cliente:')
info_cliente = pd.concat([datos_cliente, compras_cliente], axis=1)
print(info_cliente)

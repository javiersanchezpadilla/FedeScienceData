""" Dado un diccionario con datos de ventas diarias de una tienda como sigue:

        data = {
            'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', 
                      '2024-03-23', '2024-03-24'],
            'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Uvas', 
                         'Melocotones'],
            'Cantidad': [23, 15, 18, 30, 8, 20],
            'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
        }

    Tu tarea consiste en realizar las siguientes acciones:

    Creación de DataFrame: Genera un DataFrame denominado df_ventas utilizando 
    la información provista en el diccionario data.
    Cálculo de Precio Total: Añade al DataFrame df_ventas una nueva columna 
    llamada Precio Total. Esta columna debe contener el precio total de cada 
    venta, calculado como el producto de la cantidad vendida por el precio 
    unitario de cada producto.
    Guardado de Datos en CSV: Desarrolla una función titulada guardar_en_csv() 
    que exporte el DataFrame df_ventas a un archivo CSV. Nombra el archivo como 
    ventas3.csv y guárdalo en la ruta /mnt/data/. Asegúrate de que el archivo CSV 
    generado no incluya el índice del DataFrame.
"""

import pandas as pd 

data = {
    'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', 
              '2024-03-23', '2024-03-24'],
    'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Uvas', 'Melocotones'],
    'Cantidad': [23, 15, 18, 30, 8, 20],
    'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
}

ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/ventas3.csv'

def guardar_en_csv():
    df_ventas.to_csv(ruta, index=False)


df_ventas = pd.DataFrame(data)
print(df_ventas)

df_ventas['Precio Total'] = df_ventas['Cantidad'] * df_ventas['Precio']
print(df_ventas)
guardar_en_csv()

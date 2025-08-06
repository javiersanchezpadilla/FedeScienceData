""" Dado el siguiente diccionario que contiene datos de ventas diarias de una tienda:
        data = {
            'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', 
                      '2024-03-22', '2024-03-23', '2024-03-24'],
            'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 
                         'Uvas', 'Melocotones'],
            'Cantidad': [23, 15, 18, 30, 8, 20],
            'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
        }

    Realiza los siguientes pasos:

    Crea un DataFrame nombrado df_ventas  donde almacenes la información 
    antes proporcionada.
    Crea una función llamada guardar_en_excel()    que guarde este DataFrame 
    en un archivo llamado  ventas1.xlsx en la ruta siguiente: '/mnt/data/' 
    Asegúrate de no incluir el índice del DataFrame en el archivo Excel.
"""


import pandas as pd 

data = {
    'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-23', '2024-03-24'],
    'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Uvas', 'Melocotones'],
    'Cantidad': [23, 15, 18, 30, 8, 20],
    'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
}

ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/ventas1.xlsx'


def guardar_en_excel():
    df_ventas.to_excel(ruta, index=False)


df_ventas = pd.DataFrame(data)
print(df_ventas)
guardar_en_excel()


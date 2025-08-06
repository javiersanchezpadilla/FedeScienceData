""" Dada una lista de fechas en formato string 
    ['2024-01-01', '2024-02-14', '2024-03-01'] en una columna fecha de 
    una tabla llamada fechas.csv
            fecha
            2025-01-01
            2025-02-14
            2025-03-01

    Debes leer el archivo CSV 'fechas.csv' desde tu código para ello 
    emplea el método adecuado.

    Convierte estas fechas al formato datetime de Pandas con el siguiente 
    formato dia/mes/año. Almacena este DataFrame en una variable nombrada df
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/fechas.csv'
# df = pd.read_csv('fechas.csv')
df = pd.read_csv(ruta)
print(df)
print(df['fecha'][1])
print(type(df['fecha'][1]))

df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
print(df['fecha'])

# Ahora cambiamos el formato date time a cadena como se desea a dia/mes/año
df['fecha'] = df['fecha'].dt.strftime('%d/%m/%Y')
print(df['fecha'])
print(type(df['fecha'][1]))

# re convertimos a datetima
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
print(df['fecha'])
print(type(df['fecha'][1]))

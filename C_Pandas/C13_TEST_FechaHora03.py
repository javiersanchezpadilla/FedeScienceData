""" Dada una lista de fechas en formato string 
    ['01-01-2025', '14-02-2025', '01-03-2025'] en una columna 
    fecha de una tabla llamada fechas.csv
    Debes leer el archivo CSV 'fechas.csv' desde tu código para 
    ello emplea el método adecuado.
    Convierte estas fechas al formato datetime de Pandas. Con el 
    siguiente formato dia/mes/año. Almacena este DataFrame en una 
    variable nombrada   <df>     Agrega cinco días a cada fecha.
"""

import pandas as pd 


ruta = '/home/javier/Documentos/Programas/\
Python/FedeScienceData/Z_ArchivosExternos/\
fechas2.csv'

# df = pd.read_csv('fechas2.csv')
df = pd.read_csv(ruta)

print(df)

df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%m-%Y')
print(df)

df['fecha'] = df['fecha'] + pd.Timedelta(days=5)
print(df)


"""

import pandas as pd
 
# Leer el archivo CSV
df = pd.read_csv('fechas.csv')
 
# Convertir las fechas de la columna 'fecha' a tipo datetime, especificando el formato para evitar ambigüedades
df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%m-%Y')
 
# Ahora, agregar cinco días a la columna 'fecha' convertida
df['fecha'] = df['fecha'] + pd.Timedelta(days=5)
"""


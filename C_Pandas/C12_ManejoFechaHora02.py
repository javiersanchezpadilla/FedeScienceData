""" Ya convertidos los datos al tipo timestamo podemos extraer 
    informacion como:
        año (year)      mes (month)         dia (day)
        hora (hour)     minutos (minute)    segundos (second)
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Mercado+de+Valores+España.csv'

# Leemos el archivo CSV
df = pd.read_csv(ruta)

# Convertimos los datos de la columna de fecha string a fecha datestamp
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

# Vamos a tomar tres valores de la serie y vamos a extraer información
print(df['Fecha'][20])

# Extraemos el año
print('El año es:', df['Fecha'][20].year)

# Extraemos el mes
print('El mes es:', df['Fecha'][20].month)

# Extraemos el dia
print('El día es:', df['Fecha'][20].day)

# Extraemos la hora
print('La hora es:', df['Fecha'][20].hour)

# Extraemos los minutos
print('Los minutos son:', df['Fecha'][20].minute)

# Extraemos los segundos
print('Los segundos son:', df['Fecha'][20].second)


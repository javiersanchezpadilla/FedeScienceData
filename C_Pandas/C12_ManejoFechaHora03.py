""" Podemo hacer operaciones con las series del tipo TimeStamp
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Mercado+de+Valores+España.csv'

# Leemos el archivo CSV
df = pd.read_csv(ruta)

# Convertimos los datos de la columna de fecha string a fecha datestamp
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

df_mas_5_dias = df['Fecha'] + pd.Timedelta(days=5)
print(df_mas_5_dias)

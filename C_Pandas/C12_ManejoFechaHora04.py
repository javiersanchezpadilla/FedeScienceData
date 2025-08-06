""" Podemo hacer operaciones con las series del tipo TimeStamp
    En este ejemplo voy a crear dos series mas dentro del dataFrame
    una serie con diez dias mas de la fecha y otro con 2 años
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Mercado+de+Valores+España.csv'

# Leemos el archivo CSV
df = pd.read_csv(ruta)

# Convertimos los datos de la columna de fecha string a fecha datestamp
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

df['Fecha mas 5 dias'] = df['Fecha'] + pd.Timedelta(days=5)
df['Fecha mas 2 anios'] = df['Fecha'] + pd.Timedelta(days=365)

print(df)

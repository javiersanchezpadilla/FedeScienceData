""" Pruebas para manejo de las series"""

import pandas as pd  

df = pd.read_csv('/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Precipitaciones.csv')

print(df.head(2))

serie_region = df['region']
print(serie_region)
print(type(serie_region))
print(serie_region[0])
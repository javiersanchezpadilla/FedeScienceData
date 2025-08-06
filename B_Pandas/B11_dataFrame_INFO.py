"""Permite de manera rapida conocer un resumen del dataFrame."""

import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Precipitaciones.csv')

print(df.info())

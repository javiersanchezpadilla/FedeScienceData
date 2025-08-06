""" Ahora trabajaremos con las series del data frame"""

import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/Fede\
ScienceData/Z_ArchivosExternos/Precipitaciones.csv')

serie = df["region"]
print(serie.head())

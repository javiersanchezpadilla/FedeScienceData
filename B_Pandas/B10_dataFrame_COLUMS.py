"""Lista los nombres de las columnas dentro de una lista."""
import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Precipitaciones.csv')

print(df.columns)

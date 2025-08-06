""" El siguiente método permite obtener un resumen de nuestro dataframe."""
import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Precipitaciones.csv')

print(df.describe())

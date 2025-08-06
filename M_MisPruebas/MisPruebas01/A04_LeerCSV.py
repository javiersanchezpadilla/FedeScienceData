""" En este ejemplo aprenderemos a acceder a un archivo externo
    de extension csv, el archivo de trabajo es Precipitaciones.csv"""

import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/Precipitaciones.csv')

print(df)
# print(df.tail(9))
# print(df.info())
# print(df.describe())

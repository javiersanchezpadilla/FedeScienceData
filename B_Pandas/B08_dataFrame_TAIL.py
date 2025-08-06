"""En este ejercicio vamos a cargar un archivo CSV.
    El archivo de refeencia es precipitaciones y solo
    se mostrará lasúltimas lineas del arhcivo."""

import pandas as pd 


df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Precipitaciones.csv')

# Imprime las últimas cinco lineas del archivo CSV
print(df.tail(3))

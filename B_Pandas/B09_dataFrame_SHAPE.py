""" Shape no es un método es un atributo y permite conocer el número de 
    filas y columnas de un dataFrame."""

import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Precipitaciones.csv')

print('El número de filas y columnas de nuestro data frame es:', df.shape)

# Imprime las primeras y ultimas cinco lineas del archivo CSV
print(df.head())
print(df.tail())

# Imprime las primeras y ultimas tres lineas del archivo CSV
print(df.head(3))
print(df.tail(3))

"""En este ejercicio vamos a cargar un archivo CSV.
    El archivo de referencia es precipitaciones"""


import pandas as pd 

# dentro del Visual Studio tenemos directorios de trabjajos denro del entorno, por lo que
# basta con solo referenciar a partir de la posicion donde nos encontramos
#df = pd.read_csv('Z_ArchivosExternos/Precipitaciones.csv')

# Pero cuando ejecutamos por consola es precomendable referenciar toda la ruta de trabajo
# En este caso partimos la ruta de trabajo
df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Precipitaciones.csv')
print(df)


""" En este ejercicio se ordenaran y agruparan los datos de un data frame
    la agrupacion es reunir datos en funcion de valores iguales 
    obtener el raiting promedio que han obtenido las peliculas por genero
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/Top-Peliculas.csv'
df = pd.read_csv(ruta)

# Primero se agrupan las peliculas por género groupby('género')
# lo que sigue es obtener el promedio, para esto indexamos por el rating y calculamos 
# el promedio ['rating´].mean()
df_agrupado = df.groupby('género')['rating'].mean()

print(df_agrupado.head(7))


""" En este ejercicio se ordenaran y agruparan los datos de un data frame
    la agrupacion es reunir datos en funcion de valores iguales 
    obtener el total recaudado por año
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/Top-Peliculas.csv'
df = pd.read_csv(ruta)

# Primero se agrupan las peliculas por año groupby('año')
# lo que sigue es obtener la suma acumulada, para esto indexamos por el 
# rating y calculamos la suma ['recaudación(M)´].sum()
df_agrupado = df.groupby('año')['recaudación(M)'].sum()

print(df_agrupado.sort_values(ascending=False).head(7))


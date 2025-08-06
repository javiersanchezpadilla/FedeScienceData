""" Ordenar el data frame por mas de una serie

    dataFrame.sort_values (by = [serie1, serie2, ...] , ascending=False)

    En este ejemplo se ordena el data frame por dos crtierios 
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/Top-Peliculas.csv'
df = pd.read_csv(ruta)

# En este punto solo está ordenado de menor a mayor (ascendente)
df_ordenado = df.sort_values(by=['rating', 'recaudación(M)'], ascending=False)
print(df_ordenado.head(7))


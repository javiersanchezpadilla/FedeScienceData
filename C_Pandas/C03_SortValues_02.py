""" Ordenar el data frame por una serie

    dataFrame.sort_values (by = serie, ascending=False)

    En este ejemplo se ordena el data frame por el rating
    Ahora el ordenamiento es de mayor a menor
"""

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/Top-Peliculas.csv'
df = pd.read_csv(ruta)

# En este punto solo está ordenado de menor a mayor (ascendente)
df_ordenado = df.sort_values(by='rating', ascending=False)
print(df_ordenado.head(7))


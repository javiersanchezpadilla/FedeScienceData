""" Utiliza el DataFrame clima creado en el ejercicio anterior. 
    Aplica los métodos correspondientes para:
    Extraer exactamente la primera fila de 'clima'. Almacena el contenido en 
    una variable llamada head_df
    Extraer exactamente la última fila de 'clima'. Almacena el contenido en 
    una variable llamada tail_df
"""

import pandas as pd 

df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/clima.csv')
head_df = df.head(1)
tail_df = df.tail(1)
print(head_df)
print(tail_df)

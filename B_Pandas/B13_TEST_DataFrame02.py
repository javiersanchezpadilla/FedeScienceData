""" Utiliza el DataFrame datos_clima creado en el ejercicio anterior. 
    Aplica el método  describe() para explorar la estructura del DataFrame y 
    obtener un resumen estadístico de las columnas numéricas.

    Asegurese de almacenar el resultado en una variable llamada  describe_df
"""

import pandas as pd 

datos_clima = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/clima.csv')

describe_df = datos_clima.describe()
print(describe_df)

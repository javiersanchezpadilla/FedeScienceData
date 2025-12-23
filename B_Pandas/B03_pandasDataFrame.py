""" Para el uso de pandas tenemos que incorporar la libreria.

    Se incorporan dos nuevos tipos de datos
    Series ---------------------------------------------------------+
    Series ------------------------------------------+              |
    DataFrames --------------+                       |              | 
                             |                       |              |
                      +---------+------+         +--------+     +------+ 
                      |  Nombre | Edad |         | Nombre |     | Edad |
                      +---------+------|         +--------+     +------+
                      |  Pedro  |  25  |    =    | Pedro  |     |  25  |
                      |  Juan   |  39  |         | Juan   |     |  39  |
                      |  Lorena |  20  |         | Lorena |     |  20  |
                      +---------+------+         +--------+     +------+
                           DataFrame               Serie 1      Serie 2

    Se cuenta con dos series, la serie Nombre y la Serie Edad                           

    Con Pandas podremos transformar tipos de datos en DataFrames
"""

import pandas as pd    

datos = {"nombre":["pedro", "Juan", "lorena"], "edad":[25, 39, 20]}

# Incorporacion de los data frames
df = pd.DataFrame(datos)
print(df)
print(type(df))

# incorporacion de las series
# accediendo a la serie nombre
print(df["nombre"])             # Podemos acceder como si fuera un índice
print(type(df.nombre))          # tambien dentro del objeto dataFrame por su nombre de serie

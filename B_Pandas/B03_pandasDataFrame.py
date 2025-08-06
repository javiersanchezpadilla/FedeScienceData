""" Para el uso de pandas tenemos que incorporar la libreria."""

import pandas as pd    

datos = {"nombre":["pedro", "Juan", "lorena"], "edad":[25, 39, 20]}

# Incorporacion de los data frames
df = pd.DataFrame(datos)
print(df)
print(type(df))

# incorporacion de las series
# accediendo a la serie nombre
print(df["nombre"])
print(type(df.nombre))

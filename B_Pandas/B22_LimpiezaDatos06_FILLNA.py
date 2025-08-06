""" Permite reemplazar aquellos valores nulos por otros valores."""

import pandas as pd 

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, None, 25, 25],
         "Precio" : [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print('Data Frame original')
print(df)

print('Data Frame con datos cambiados')
# Para la serie "Cantidad_vendida" los valores nulos se convertirar a cero
# Para la serie "Precio" los valores nulos se cambiaran al promedio mismo de la serie
valores_nuevos = {"Cantidad_vendida" : 0, "Precio" : df["Precio"].mean() }
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)

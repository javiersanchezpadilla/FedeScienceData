import pandas as pd 

""" Elimina registros duplicados con base a una serie como referencia"""

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, 0, 25, 25],
         "Precio" : [20.50, 15.00, 19.33, 22.50]}

df = pd.DataFrame(data)

print("DATA FRAME ORIGINAL")
print(df)

print("DATA FRAME SIN DUPLICADOS")
df_unicos = df.drop_duplicates(subset="id_producto")
print(df_unicos)

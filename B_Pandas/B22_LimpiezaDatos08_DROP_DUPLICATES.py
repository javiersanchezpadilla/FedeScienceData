import pandas as pd 

""" Elimina registros que en su totalidad esten duplicados, en caso de existir
    diferencia en una de los valore no elimina el registro.
    En caso de eliminar los duplicados deja solo un original"""

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, 0, 25, 25],
         "Precio" : [20.50, 15.00, 22.50, 22.50]}

df = pd.DataFrame(data)

print("DATA FRAME ORIGINAL")
print(df)

print("DATA FRAME SIN DUPLICADOS")
df_unicos = df.drop_duplicates()
print(df_unicos)


import pandas as pd 

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, None, 25, 25],
         "Precio" : [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print('Data Frame original')
print(df)

print('Data Frame con eliminados')
df_eliminados = df.dropna()
print(df_eliminados)

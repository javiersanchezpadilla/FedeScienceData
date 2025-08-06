import pandas as pd

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, None, 25, 25],
         "Precio" : [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print(df)

# RECORDAR QUE TENEMOS UN RESUMEN RAPIDO CON DataFrane,INFO()<<<<<
print(df.info())

# IDENTIFICAR LOS VALORES NULOS <<<<<<<<<<<<
print(df.isnull())

# EN CASO DE UNA TABLA MUY GRANDE<<<<<<<<<<<<<<<
print(df.isnull().sum())

# ELIMINAR LOS VALORES NULOS <<<<<<<<<<<<<<<<<
nuevo_DataFrame = df.dropna()
print(nuevo_DataFrame)

# RELLENAR CON CEROS Y VALOR PROMEDIO <<<<<<<<<<<<<<<<
valores_nuevos = {"Cantidad_vendida" : 0, "Precio" : df["Precio"].mean() }
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)

# CAMBIAR EL TIPO DE DATO DE CANTIDAD_VENDIDA DE FLOTANTE A ENTERO <<<<<<<
df_rellenados["Cantidad_vendida"] = df_rellenados['Cantidad_vendida'].astype(int)
print(df_rellenados)

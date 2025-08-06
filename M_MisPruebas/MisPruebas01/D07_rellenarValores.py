import pandas as pd 

datos = {'Clave producto': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
         'Nombre producto': ['Lapiz', 'Pluma', 'Borrador', 'Calculadora', 'Telefono',
                             'teclado', 'raton', 'jabon', 'cuchara', 'plato', 'Tenedor'],
         'Cantidad Vendida': [2, 1, 3, 4, 1, 1, None, 1, None, None, None ],
         'Precio' : [10, 100, 15, None, 20, None, None, 25, 10, 13, 20]}

df = pd.DataFrame(datos)
print(df)

#print(df.info())
# crear un data frame eliminando los valores incompletos
df_sin_nan = df.dropna()
print(df_sin_nan)

# Reemplazar por Nan por ceros y el valor promedio
nuevos_valores = {'Cantidad Vendida':0, 'Precio': df['Precio'].mean()}

# valores_nuevos = {"Cantidad Vendida" : 0, "Precio" : df["Precio"].mean() }
df_rellenados = df.fillna(nuevos_valores)
print(df_rellenados)

# cambiando el dato de precio de flotante a entero
df_rellenados['Precio'] = df_rellenados['Precio'].round(0).astype(int)
print(df_rellenados)

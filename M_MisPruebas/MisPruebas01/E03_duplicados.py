import pandas as pd 

valores = {'Producto': [1, 2, 3, 4, 1, 1],
         'Cantidad': [ 1, 1, 1, 1, 2, 3]}

df = pd.DataFrame(valores)
print(df)

# ELIMINA REGISTROS DUPLICADOS <<<<<<<<<<<<<<<<<
elimina_duplicados = df.drop_duplicates()
print(elimina_duplicados)

# ELIMINA BAJO UN CRITERIO <<<<<<<<<<<<<<<<
elimina_dupli_criterio = df.drop_duplicates(subset='Producto')
print(elimina_dupli_criterio)



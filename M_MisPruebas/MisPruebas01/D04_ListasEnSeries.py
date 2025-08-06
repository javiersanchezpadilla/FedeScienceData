import pandas as pd 

valores = {'Nombre': ['Juan', 'Carlos', 'Rocio'],
           'Edad'  : [20, 25, 18]}

mi_lista = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(valores)
print(df)

serie_nombre = df['Nombre']
serie_edad = df['Edad']

print(serie_nombre)
print(type(serie_nombre))

print(serie_edad)
print(type(serie_edad))

df_lista = pd.Series(mi_lista)
print(df_lista)
print(type(df_lista))
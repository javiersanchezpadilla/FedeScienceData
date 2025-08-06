import pandas as pd 

lista1 = { 'ID': [1, 2, 3],
           'Nombre': ['Ana', 'Luis', 'Carlos']}

lista2 = { 'ID': [1, 2, 4],
           'Edad': [25, 30, 22]}

df1 = pd.DataFrame(lista1)
df2 = pd.DataFrame(lista2)
print('El primer data frame\n', df1)
print('\nEl segundo data frame\n', df2)

# Sola las intersecciones del conjunto
df_fusionado = pd.merge(df1, df2, on='ID')
print('Data Frame fusionado\n', df_fusionado)

# Usando how='inner'
df_fusionado2 = pd.merge(df1, df2, how='inner')
print('Data frame con how=inner\n', df_fusionado2)

# usando how='left'
df_fusionado3 = pd.merge(df1, df2, how='left')
print(df_fusionado3)

# usando how='right'
df_fusionado4 = pd.merge(df1, df2, how='right')
print(df_fusionado4)

# por referencia de los índices
df_fusionado5 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df_fusionado5)



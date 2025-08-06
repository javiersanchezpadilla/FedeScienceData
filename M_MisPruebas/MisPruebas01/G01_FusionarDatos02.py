import pandas as pd 

df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Ana', 'Luis', 'Carlos']})

df2 = pd.DataFrame({'ID':[1, 2, 4],
                    'Edad': [25, 30, 22]})

print('Data frame 1')
print(df1)
print('\nData frame 2')
print(df2)

print('\nData frame combinado')
df_combinado = pd.merge(df1, df2, on='ID')
print(df_combinado)

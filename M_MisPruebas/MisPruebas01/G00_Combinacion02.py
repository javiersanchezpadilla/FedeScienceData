import pandas as pd

# Creación del DataFrame df_a
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})

print(df_b)
df_b.set_index('id', inplace=True)
print(df_b)
print(df_b.loc[2])

df_combinado = df_a.join(df_b)

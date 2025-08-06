""" Dados dos DataFrames, df_a y df_b. df_a

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
    df_b.set_index('id', inplace=True)
    
    Utiliza el método join() para combinar df_a y df_b en un nuevo 
    DataFrame llamado df_combinado, usando el argumento por defecto de how.
"""

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

df_b.set_index('id', inplace=True) 

print('Primer data frame')
print(df_a)

print('\nSegundo data frame')
print(df_b)

print('Union de los data frame')
df_combinado = df_a.join(df_b)
print(df_combinado)




""" Partiendo del DataFrame df mencionado anteriormente:
    Datos proporcionados
    data = {
        'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad': [25, 30, 22, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
    }

    Realiza las siguientes operaciones:
        * Crea un dataframe llamado df
        * Agrega una nueva columna llamada Edad_en_10_años que contenga 
          la edad de las personas dentro de 10 años.
        * Modifica la columna Ciudad para que todas las ciudades estén 
          en mayúsculas.
        * Crea una nueva columna Es_Mayor_de_25 que contenga valores 
          booleanos: True si la persona tiene 25 años o más, y False en caso contrario.
"""
import pandas as pd 

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

# Crea un dataframe llamado df
df = pd.DataFrame(data)
print('Impresion del data frame original')
print(df)

# Agrega una nueva columna llamada Edad_en_10_años que contenga 
# la edad de las personas dentro de 10 años.
print('\nEl data frame con la columna agregada')
df['Edad_en_10_años'] = df['Edad'] + 10
print(df)

# Modifica la columna Ciudad para que todas las ciudades estén 
# en mayúsculas.
print(type(df['Ciudad']))
# print(dir(df['Ciudad'].str))
df['Ciudad'] = df['Ciudad'].str.upper()
print(df)

# Agregar nueva columna llamada Es_Mayor_de_25 que contenga valores 
# booleanos: True si la persona tiene 25 años o más, y False en caso contrario.
criterio = df['Edad'] >= 25
print(criterio)
df['Es_Mayor_de_25'] = criterio
print(df)

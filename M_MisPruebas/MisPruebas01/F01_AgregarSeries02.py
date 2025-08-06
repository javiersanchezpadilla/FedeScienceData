import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
print(df)

# CREAR UNA NUEVA SERIE DENTRO DEL DATA FRAME
print('Agregamos una nueva serie a nuestro data frame:')
df['Salario'] = [10000, 20000, 25000, 30000]
print(df)

# MODIFICAR LOS DATOS DENTRO DE LA SERIE
print('\nModificamos los datos de  nuestra serie de edades dentro del data frame')
df['Salario'] = df['Salario'] + 2000
print(df)

# ASIGNAR A UNA VARIABLE UNA SERIE DEL DATA FRAME
print('\nAlmacenamos los datos de una serie en una variable')
serie_nombres = df['Nombre']
print(serie_nombres)


# FILTRADO DE DATOS EN EL DATA FRAME
# queremos ver del data frame aquellos registros donde la edad es > 25
print('\nFiltrado de datos dentro del data frame, solo los mayores de 25 años:')
filtro = df['Edad'] > 25
mayores_25 = df[filtro]
print(mayores_25)


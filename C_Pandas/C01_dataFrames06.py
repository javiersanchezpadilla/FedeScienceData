""" Manejo de data frames.

    ESTE PROGRAMA CONTIENE TODOS LOS TEMAS ANTERIORES

    * Agregando nuevas series a nuestro data frame
    * Mdificando los datos de una serie
    * Crear series a partir de nuestras series del data frame
    * Filtrado de series dentro del data frame
        Para este ejercicio se hace de dos maneras
        de forma directa y luego mediante el uso de una variable
    """

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanej']
}


df = pd.DataFrame(data)
print(df)

# Agregando nuevas series a nuestro data frame
# Simplemente como en los diccionarios, agragamos la columna y sus datos
print('Agregamos una nueva serie a nuestro data frame:')
df['Salario'] = [10000, 20000, 25000, 30000]
print(df)

# Para modificar los datos de la serie
print('\nModificamos los datos de  nuestra serie de edades dentro del data frame')
df['Salario'] = df['Salario'] + 2000
print(df)

# Seleccionar una columna o serie en particular y almacenarla en una 
# variable, la variable ahora es del tipo serie
print('\nAlmacenamos los datos de una serie en una variable')
serie_nombres = df['Nombre']
print(serie_nombres)

# filtrado de data frame
# queremos ver del data frame aquellos registros donde la edad es > 25
print('\nFiltrado de datos dentro del data frame, solo los mayores de 25 años:')
mayores_25 = df[df['Edad'] > 25]
print(mayores_25)

# El mismo filtrado de arriba pero haciendolo paso a paso mediamte variables
print('\nEl mismo filtrado pero con variables, creamos la variable edades')
print('Que contendra solo la serie de las edades del data frame')
edades = df['Edad']
print(edades)
print('Ahora aplicamos mediante la varible el filtro')
mayores_25_ver2 = df[edades > 25]
print(mayores_25_ver2)


# Es importante siempre en todo momento verificar los tipos de datos que estamos
# trabajando 
print('\n\n **************************************')
print('Tipo de dato de <df>', type(df))
print('Tipo de dato de <serie_nombres>', type(serie_nombres))
print('Tipo de dato de <mayores_25>', type(mayores_25))
print('Tipo de dato de <edades>', type(edades))
print('Tipo de dato de <mayores_25_ver>', type(mayores_25_ver2))
    

""" Manejo de data frames.
    Crear series a partir de nuestras series del data frame.
    De nuestro data frme podemos tomar una serie y asignarla a otra variable
    del tipo data frame"""

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanej'],
        'Salario' : [10000, 20000, 25000, 30000]
}

df = pd.DataFrame(data)
print(df)

# Seleccionar una columna o serie en particular de nuestro data frame
# y almacenarla en una variable, la variable ahora es del tipo serie

print('\nAlmacenamos los datos de una serie en una variable')
serie_nombres = df['Nombre']
print(serie_nombres)


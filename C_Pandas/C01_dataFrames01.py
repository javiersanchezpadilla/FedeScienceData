""" Manejo de data frames.
    Agregando nuevas series a nuestro data frame"""

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanej']
}

df = pd.DataFrame(data)
print(df)

# Simplemente como en los diccionarios, agregamos la columna y sus valores
df['Salario'] = [10000, 20000, 25000, 30000]
print('\n')
print(df)


""" Manejo de data frames.
    Mdificando los datos de una serie"""

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanej']
}


df = pd.DataFrame(data)
print ('Data frame original')
print(df)

df['Salario'] = [10000, 20000, 25000, 30000]

print('\nData frame con una nueva columna de salario')
print(df)

# Para modificar los datos de la serie
print('\nModificamos los datos de  nuestra serie de Salarios dentro del data frame')
df['Salario'] = df['Salario'] + 2000
print(df)


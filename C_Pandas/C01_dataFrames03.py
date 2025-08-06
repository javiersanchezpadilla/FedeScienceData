""" Manejo de data frames.
    Agregando una nueva serie con datos de otra serie modificada"""

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanej']
}


df = pd.DataFrame(data)
print ('Data frame original')
print(df)

df['Edad Avanzada'] = df['Edad']+50

print('\nData frame con una nueva columna de salario')
print(df)

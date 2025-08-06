""" Manejo de data frames.
    Filtrado de series dentro del data frame
        Para este ejercicio se hace de dos maneras
        de forma directa y luego mediante el uso de una variable
    """

import pandas as pd 

data = {
        'Nombre' :  ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' :    [25, 30, 22, 27],
        'Ciudad' :  ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanejo'],
        'Salario' : [10000, 20000, 25000, 30000]
}

df = pd.DataFrame(data)
# filtrado de data frame
# queremos ver del data frame aquellos registros donde la edad es > 25
print('\nFiltrado de datos dentro del data frame, solo los mayores de 25 años:')
mayores_25 = df[df['Edad'] > 25]
print(mayores_25)

# El mismo filtrado de arriba pero haciendolo paso a paso mediante la 
# creación de una variable del tipo serie
edades = df['Edad']
print('\n')
print(edades)
print('\nAhora aplicamos mediante la varible el filtro')
mayores_25_ver2 = df[edades > 25]
print(mayores_25_ver2)


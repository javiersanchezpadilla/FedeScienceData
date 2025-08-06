""" Dado el DataFrame df_empleados creado en el ejercicio anterior:
    La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Para explorar sus atributos principales: shape, columns, y index.

    Utilizando las siguientes variables respectivamente: shape_df, columns_df, index_df 
    Imprime los resultados de cada exploración para demostrar tu comprensión de la estructura de los DataFrames y las Series en Pandas.
    El resultado esperado es el siguiente: """

import pandas as pd 

datos = {"nombre":['Ana', 'Luis', 'Carlos'], "edad":[30, 25, 40]}

edades = pd.DataFrame(datos)
shape_df = edades.shape
columns_df = edades.columns
index_df = edades.index

print(shape_df)
print(columns_df)
print(index_df)



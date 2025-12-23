""" Dado el DataFrame df_empleados creado en el ejercicio anterior:
    La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Para explorar sus atributos principales: shape, columns, y index.

    Utilizando las siguientes variables respectivamente: shape_df, columns_df, index_df 
    Imprime los resultados de cada exploración para demostrar tu comprensión de la estructura de los DataFrames y las Series en Pandas.
    El resultado esperado es el siguiente: """

import pandas as pd 

datos = {"nombre":['Ana', 'Luis', 'Carlos'], "edad":[30, 25, 40]}

df_empleados = pd.DataFrame(datos)

shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index

print('Shape', shape_df)
print('Colums', columns_df)
print('Index', index_df)

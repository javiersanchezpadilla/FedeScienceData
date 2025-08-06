""" Dado el DataFrame df_empleados creado en el ejercicio anterior: 
    La columna nombre debe contener los nombres de tres empleados: 
    'Ana', 'Luis' y 'Carlos', la columna edad debe contener las edades 
    correspondientes: 30, 25 y 40

    Para explorar sus atributos principales: shape, columns, y index.
    Utilizando las siguientes variables respectivamente: 
    shape_df, columns_df, index_df 
    Imprime los resultados de cada exploración para demostrar tu comprensión 
    de la estructura de los DataFrames y las Series en Pandas.
    El resultado esperado es el siguiente:
    (3, 2)
                Index(‘nombre’. ‘edad’), dtype=’oject’)
                RangeIndex(start=0, stop=3, step=1)
    No se preocupes si en este momento no entiendes del todo estos resultados, 
    recordemos que solo estamos explorando"""

import pandas as pd 

datos = {"nombre":['Ana', 'Luis', 'Carlos'], "edad":[30, 25, 40]}

df = pd.DataFrame(datos)
print(df)

shape_df = df.shape
print(shape_df)

columns = df.columns
print(columns)

index_df = df.index
print(index_df)
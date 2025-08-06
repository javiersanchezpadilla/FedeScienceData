"""Ejercicio Tipos de Datos en Pandas 1.
    Utilizando la biblioteca Pandas, crea un DataFrame llamado df_empleados 
    que contenga dos columnas: nombre y edad.
    La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Finalmente, muestra el DataFrame df_empleados utilizando la función print()."""

import pandas as pd 

datos = {"nombre":['Ana', 'Luis', 'Carlos'], "edad":[30, 25, 40]}

df_empleados = pd.DataFrame(datos)
print(df_empleados)

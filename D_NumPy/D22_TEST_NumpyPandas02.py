""" Crea un DataFrame de Pandas llamado mi_dataframe con 
    dos columnas: "Frutas" y "Cantidad". Identico al 
    ejercicio anterior.
    La columna "Frutas" debe contener los valores "Manzana", 
    "Banana" y "Cereza".
    La columna "Cantidad" debe contener los números 5, 8 y 3.

    Luego, filtra las filas donde la cantidad sea mayor a 4, 
    almacena el resultado en una variable llamada: 
    mi_dataframe_filtrado
    Convierte el resultado en un array de NumPy. Guarda el 
    array resultante en una variable llamada array_filtrado
    En esta lección podrás recordar como filtrar datos en Pandas:
    Flitrado de series en Pandas
"""

import numpy as np 
import pandas as pd 

mi_dataframe = pd.DataFrame({ 'Frutas' : ['Manzana', 'Banana', 'Cereza'],
                             'Cantidad': [5, 8, 3]})

filtro = mi_dataframe['Cantidad'] > 4
mi_dataframe_filtrado = mi_dataframe[filtro] 

array_filtrado = mi_dataframe_filtrado.to_numpy()

print('Mi dataframe original:\n', mi_dataframe)
print('El data frame filtrado donde cantidad > 4\n', mi_dataframe_filtrado)
print('El array de numpy del data frame filtrado:\n', array_filtrado)

""" Crea un DataFrame de Pandas llamado mi_dataframe con 
    dos columnas: "Frutas" y "Cantidad".
    La columna "Frutas" debe contener los valores 
    "Manzana", "Banana" y "Cereza".
    La columna "Cantidad" debe contener los números 5, 8 y 3 
    respectivamente.
    Luego, convierte este DataFrame en un array de NumPy 
    y guárdalo en una variable llamada array_frutas.
"""

import pandas as pd 
import numpy as np 

mi_dataframe = pd.DataFrame({ 'Frutas' : ['Manzana', 'Banana', 'Cereza'],
                             'Cantidad': [5, 8, 3]})

array_frutas = mi_dataframe.values
print('Data Frame de Pandas:\n', mi_dataframe)
print('Array convertido del data frame:\n', array_frutas)

print(type(array_frutas[0, 0]))
print(type(array_frutas[0, 1]))

print(array_frutas[0,0])
print(array_frutas[0,1])

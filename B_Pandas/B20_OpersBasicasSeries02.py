""" Vamos a realizar algunas de las operaciones básicas con las series de datos
    Para sumar todos los valores de la serie, puedo hacerlo de esta forma"""
import pandas as pd 

serie = pd.Series([10, 20, 30, 40, 50])
print(serie)

# Le sumamos mil a cada elemento de la seria
serie = serie + 100
print(serie)


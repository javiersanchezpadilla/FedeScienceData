""" Vamos a realizar algunas de las operaciones básicas con las series de datos
    Por ejemplo para sumar valores, puedo directamente tomar un valor o varios 
    valores y afectarlos directamente"""
import pandas as pd 

serie = pd.Series([10, 20, 30, 40, 50])
print(serie)

serie[0] = serie[0] + 100
print(serie)


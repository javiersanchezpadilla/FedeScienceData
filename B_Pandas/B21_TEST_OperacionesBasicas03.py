""" Considera una serie de pandas llamada serie_grande que contiene los números 
    del 1 al 10 o mayor al 10. Obten su item 9 y haya su raiz cuadrada.
    Imprime el resultado.
"""
import pandas as pd 

serie_grande = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(serie_grande[8] ** 0.5)

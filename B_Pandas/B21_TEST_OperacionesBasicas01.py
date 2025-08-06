""" Crea dos series de pandas utilizando listas de Python.
    Puedes crear ambas series con los números enteros de tu elección solamente asegurate 
    de que la serie 1 y la serie 2 las almacenes en variables nombradas: 
    serie1 y serie2 respectivamente.
    Luego, suma ambas series y asigna el resultado a una variable llamada serie_sumada. 
    Imprime el resultado de serie_sumada.
"""
import pandas as pd 

serie1 = pd.Series([10, 20, 30, 40, 50, 60])
serie2 = pd.Series([100, 110, 120, 130, 140, 150])

serie_sumada = serie1 + serie2
print(serie_sumada)


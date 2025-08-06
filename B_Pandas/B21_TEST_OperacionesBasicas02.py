""" Dada una serie de pandas llamada serie_numerica que contienga los números 
    de tu preferencia.
    Realiza las siguientes operaciones matemáticas y guarda los resultados en 
    variables separadas:
    Multiplica serie_numerica por 2 y guarda el resultado en serie_doble.
    Divide serie_numerica por 10 y guarda el resultado en serie_dividida.
    Imprime los resultados de serie_doble y serie_dividida.
"""
import pandas as pd 

serie_numerica = pd.Series([10, 20, 30, 40, 50, 60, 70])
serie_doble = serie_numerica * 2
serie_dividida = serie_numerica / 10

print(serie_doble)
print(serie_dividida)

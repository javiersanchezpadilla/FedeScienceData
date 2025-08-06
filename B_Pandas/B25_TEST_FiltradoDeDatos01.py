""" Crea una serie de Pandas llamada:  serie_numeros   que contenga los números del 1 al 20.
Luego, escribe un código que filtre y muestre solo aquellos números que sean mayores que 10.
Utiliza una variable llamada filtro para almacenar la serie  filtrada.
"""
import pandas as pd 

serie_numeros = pd.Series([x for x in range(1,21)])
print(serie_numeros)
# criterio = serie_numeros > 10
# print(criterio)
# filtro = serie_numeros[criterio]
# print(filtro)

# Version 02 de los mismo de arriba 
filtro = serie_numeros[serie_numeros > 10]
print(filtro)

""" Dada una serie de Pandas que contiene los siguientes valores: [18, 22, 7, 9, 15, 8],
    filtra y muestra solo aquellos valores que sean pares.
    Primero, crea una serie de valores booleanos que represente la condición. 
    Nombra a esta variable como: condicion_valores_pares
    Luego aplica esta serie para filtrar los valores originales.
"""

import pandas as pd 

valores = pd.Series([18, 22, 7, 9, 15, 8])
condicion_valores_pares = valores % 2 == 0
print(condicion_valores_pares)
print(valores[condicion_valores_pares])


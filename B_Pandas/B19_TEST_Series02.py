""" Crea una serie en Pandas a partir de la lista [10, 20, 30, 40] 
    con índices personalizados ['a', 'b', 'c', 'd']. Llama a esta serie 
    serie_con_indices.
    Crea una variable llamada valor_c  donde almacenes el valor asociado al índice 'c'
    Crea una función llamada imprimir_valor_c  que se capaz de mostrar el valor asociado 
    al índice 'c'."""

import pandas as pd 

def imprimir_valor_c(serie_parametro):
    print(serie_parametro['c'])


lista = [10, 20, 30, 40]
indices = ['a', 'b', 'c', 'd']

serie_con_indices = pd.Series(lista, indices)
print(serie_con_indices)

valor_c =serie_con_indices['c']
imprimir_valor_c(serie_con_indices)


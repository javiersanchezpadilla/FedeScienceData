""" En este ejemplo vamos a convertir una lista de python a una serie.
    pero ademas le vamos a asignar un índice distinto al que genera
    por defecto.
    
    pandas.Series(lista_de_datos, lista_de_indices)                """

import pandas as pd 


datos_en_lista = [10, 20, 30, 40, 50, 60]
indice_para_la_lista = ["a", "b", "c", "d", "e", "f"]

serie_convertida = pd.Series(datos_en_lista, indice_para_la_lista)

print(serie_convertida)
print('\n Accediendo a los elemento del índice personalizado')
print('Primer  elemento',serie_convertida["a"])
print('Segundo elemento',serie_convertida["b"])
print('Tercer  elemento',serie_convertida["c"])
print('Cuarto  elemento',serie_convertida["d"])
print('Quinto  elemento',serie_convertida["e"])
print('Sexto   elemento',serie_convertida["f"])


"""En este ejercicio analizaremos los tipos de datos que se
    manejan y distinguiremos entre los tipos de datos serie
    con los datos que contiene cada serie                  """

import pandas as pd 


datos_en_lista = [10, 20, 30, 40, 50, 60]
indice_para_la_lista = ["a", "b", "c", "d", "e", "f"]

serie_convertida = pd.Series(datos_en_lista, indice_para_la_lista)

print(serie_convertida)
print('\n Accediendo a los elemento del índice personalizado')

print('Tercer  elemento',serie_convertida["c"])
print('Sexto   elemento',serie_convertida["f"])

print('Imprimiento del tipo de dato de la serie', type(serie_convertida))
print('Tipo de dato de un elemento de la serie', type(serie_convertida["c"]))
print('Tipo de dato de un elemento de la serie', type(serie_convertida["f"]))

""" En este ejemplo vamos a convertir una lista de python a una serie.
    el método a usar el 
    
    pandas.Series(listaDeDatos)                                       """

import pandas as pd 


datos_en_lista = [10, 20, 30, 40, 50, 60]

serie_convertida = pd.Series(datos_en_lista)

print(serie_convertida)


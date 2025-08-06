""""Crea una serie en Pandas a partir de la siguiente lista de números: 
    [4, 7, -5, 3]. Llama a esta serie mi_serie. 
    Imprime mi_serie para ver el resultado.
"""
import pandas as pd 

lista = [4, 7, -5, 3]
mi_serie = pd.Series(lista)
print(mi_serie)

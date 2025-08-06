""" Utiliza el diccionario {'a': 30, 'b': 70, 'c': 160, 'd': 50} para crear una 
    serie en Pandas, la cual llamarás serie_desde_diccionario.
    Luego, accede a los valores asociados a los índices 'a' y 'd', sumándolos. 
    Almacena esta suma en la variable suma_ad
    Crea una función llamada: imprimir_suma_ad() que se encargue de imprimir el 
    valor de suma_ad"""

import pandas as pd 

def imprimir_suma_ad(valor):
    print(valor)

mi_diccionario = {'a': 30, 'b': 70, 'c': 160, 'd': 50}

serie_desde_diccionario = pd.Series({'a': 30, 'b': 70, 'c': 160, 'd': 50})
suma_ad = serie_desde_diccionario['a'] + serie_desde_diccionario['d']
imprimir_suma_ad(suma_ad)

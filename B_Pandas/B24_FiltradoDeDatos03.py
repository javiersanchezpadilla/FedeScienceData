""" Filtrado de datos con cadenas.

    Aquí es mas complicado debido a que no existen metodos en las series que permitan
    el manejo de cadenas, debemos solicitar ayuda para poder analizar los metodos 
    disponibles"""

import pandas as pd 

serie = pd.Series(['platano', 'pera', 'piña', 'manzana', 'melon', 'kiwi'])
print(serie)

# Vamos a ver de que tipo es nuestra variable serie
# print(type(serie))

# Vamos a ver el tipo de uno de los elementos de la serie
# print(type(serie[0]))
# print(dir(serie))
# print(help(serie.str))
 
iltro = serie.str.contains("m")
print()

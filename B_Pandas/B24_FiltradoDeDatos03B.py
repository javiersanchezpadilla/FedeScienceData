""" Filtrado de datos con cadenas.

    Aquí es mas complicado debido a que no existen metodos en las series que permitan
    el manejo de cadenas, debemos solicitar ayuda para poder analizar los metodos 
    disponibles
    Vamos a tratar de dar otra solución """


import pandas as pd 

serie = pd.Series(['platano', 'pera', 'piña', 'manzana', 'melon', 'kiwi'])
print(serie)

lista_resultado = []

for el_valor in serie:
    print(el_valor)
    for letra in el_valor:
        if letra == "m":
            lista_resultado.append(el_valor)
            break

print(lista_resultado)


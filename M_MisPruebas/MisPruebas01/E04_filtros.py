import pandas as pd 

serie = pd.Series([5, 10, 15, 20, 25])

# FILTRADO DE SERIES <<<<<<<<<<<<<<<<<<<
criterio = serie > 15
serie_filtrada = serie[criterio]

print(criterio)     # Asi funciona el filtro
print(serie_filtrada)

# FILTRANDO CADENAS <<<<<<<<<<<<<<<<<<<<<<<<
serie_cadenas = pd.Series(['platano', 'pera', 'piña', 'manzana', 'melon', 'kiwi'])
print(serie_cadenas)

# Vamos a ver de que tipo es nuestra variable serie
print(type(serie_cadenas))

# Vamos a ver el tipo de uno de los elementos de la serie
print(type(serie_cadenas[0]))

# Mi serie contiene strings pero mi serie es una variable del tipo serie
# El objetivo es filtrar los elementos y buscar si algunos de ellos cumplen alguna 
# condición, por ejemplo buscar o filtrar aquellos que tengan la letra “m” en su string, 
# el problema es que para esto se requieren aplicar métodos de string sin embargo el 
# tipo o clase Serie no contiene esos métodos para manejo de strings. Esto es los 
# objetos son string, pero el tipo de dato es una serie. Existe un método para la 
# clase string <str> que llama contain (contiene) y permite buscar en un string si 
# existe una subcadena pero no lo puedo utilizar porque serie no es un string.

# Imprimimos los métodos disponibles en la clase serie, vamos a ver que no existe algún 
# método contains dentro de los métodos disponibles

# print(dir(serie_cadenas))
# print(help(serie_cadenas.str))
filtro_letra = serie_cadenas.str.contains("m")
print(filtro_letra)
serie_filtro_Cadena = serie_cadenas[filtro_letra]
print(serie_filtro_Cadena)

# SOLUCION MANUAL

# serie = pd.Series(['platano', 'pera', 'piña', 'manzana', 'melon', 'kiwi'])
# print(serie)

# lista_resultado = []

# for el_valor in serie:
#     print(el_valor)
#     for letra in el_valor:
#         if letra == "m":
#             lista_resultado.append(el_valor)
#             break

# print(lista_resultado)

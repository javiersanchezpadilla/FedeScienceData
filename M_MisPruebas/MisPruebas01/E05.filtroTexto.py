import pandas as pd 

serie = pd.Series(['platano', 'pera', 'piña', 'manzana', 'melon', 'kiwi'])
print(serie)

#print(type(serie))
# print(type(serie[1]))

filtro = serie.str.contains('m')
serie_filtrada = serie[filtro]
print(serie_filtrada)

lista_de_frutas_con_m = []

for fruta in serie:
    for letra in fruta:
        if letra == 'm':
            lista_de_frutas_con_m.append(fruta)
            break

print(lista_de_frutas_con_m)



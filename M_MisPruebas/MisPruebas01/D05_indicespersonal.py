import pandas as pd 

lista = [1, 2, 3, 4, 5, 6]
indices = ['a', 'b', 'c', 'd', 'e', 'f']

mi_serie = pd.Series(lista, indices)
print(mi_serie)

print(mi_serie['a'])
print(mi_serie['b':'e'])

otra_serie = pd.Series(lista)
print(otra_serie)
print(otra_serie[0])
print(otra_serie[1:5])
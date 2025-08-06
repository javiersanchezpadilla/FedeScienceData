

import pandas as pd 

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
indice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

serie = pd.Series(lista, indice)
print(serie)

print(serie.loc[5:8])




import pandas as pd 

serie = pd.Series([5, 10, 15, 20, 25])

criterio = serie > 15
serie_filtrada = serie[serie > 15]

print(criterio)     # Asi funciona el filtro
print(serie_filtrada)


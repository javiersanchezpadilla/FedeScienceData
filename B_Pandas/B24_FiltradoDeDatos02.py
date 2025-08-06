""" PREGUNTA 01, ¿cuántos de los valores de la serie son mayores a 15?
    Construimos una condición y luego la aplicamos a nuestra serie
"""

import pandas as pd 

serie = pd.Series([5, 10, 15, 20, 25])

filtro  = serie > 15
serie_filtrada = serie[filtro]
print(serie_filtrada)

# Revismos el contenido de la variable filtro
print(filtro)

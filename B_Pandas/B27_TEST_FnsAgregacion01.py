""" Crea una serie de Pandas a partir de la siguiente lista de edades 
    edades = [23, 30, 26, 27, 22, 24, 25, 28]. 
    Luego, utiliza la función adecuada para calcular el promedio de estas edades. 
    Almacena el promedio en una variable llamada: promedio_edades
"""

import pandas as pd 

edades = [23, 30, 26, 27, 22, 24, 25, 28]
serie = pd.Series(edades)
promedio_edades = serie.mean()
print(promedio_edades)

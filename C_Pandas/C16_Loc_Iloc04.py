""" Acceder a elementos especificos en nuestro data frame
    a traves de SEGMENACION
    Extrayendo mediante valores boleanos
    El númerod de valores boleanos debe ser equivalente
    al total de las filas
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

# como LOC extrae por filas le estamos diciendo que solo
# fila1 = False, fila2 = True, file3 = False
# Solo extraera la fila dos
print(df.loc[[False, True, False]])

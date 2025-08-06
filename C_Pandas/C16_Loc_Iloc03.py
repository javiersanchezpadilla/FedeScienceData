""" Acceder a elementos especificos en nuestro data frame
    a traves de SEGMENACION
    Extrayendo de la fila2 a la fila 3
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])


print(df.loc['fila2':'fila3'])

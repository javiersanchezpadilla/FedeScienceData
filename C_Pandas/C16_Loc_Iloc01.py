""" Acceder a elementos especificos en nuestro data frame
   Extrayendo la fila 1 mediante     LOC
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

# Extrayendo los datos de una fila
print(df.loc['fila1'])

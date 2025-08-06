""" Extrayendo columnas mediante el uso de LOC
    
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])


print(df.loc[:, ['Col1', 'Col2']])

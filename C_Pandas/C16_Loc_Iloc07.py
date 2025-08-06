""" Extrayendo columnas mediante el uso de ILOC
    basado en las posiciones ya no en etiquetas
    ILOC Básicamente es lo mismo que LOC, la diferencia 
    es que LOC hace referencia alas etiquetas, 
    mientras que ILOC se basa en las posiciones del índice.
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

print(df.iloc[0])

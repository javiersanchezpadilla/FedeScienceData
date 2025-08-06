""" Extrayendo columnas mediante el uso de ILOC
    basado en las posiciones ya no en etiquetas
    ILOC indicando un rango de INDICES
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

print(df.iloc[1:3])     # Desde el índice 1 hasta el 3-1 (2)


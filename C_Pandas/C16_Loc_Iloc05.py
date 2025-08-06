""" Acceder a elementos especificos en nuestro data frame
    a traves de CONDICIONES ESPECÍFICAS.
"""

import pandas as pd 

df = pd.DataFrame({
    'Col1' : [100, 200, 300],
    'Col2' : [400, 500, 600],
    'Col3' : [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

# Seleccionar solo aquellas filas donde el valor
# de columna 1 > 150
print(df.loc[df['Col1'] > 150])

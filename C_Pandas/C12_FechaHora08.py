""" Modificar la frecuencia de afectacion de periods 
    con una frecuencia e cadacincodias
    freq ='5D'
"""

import pandas as pd 

fechas = pd.Series(pd.date_range('20250101', periods=6, freq='5D'))
print(fechas)

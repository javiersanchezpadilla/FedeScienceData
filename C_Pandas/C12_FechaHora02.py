""" Modificar la frecuencia de afectacion de periods

    pandas.Series(pandas.date_range('20250101', periods=6, frec='D'))
    
    Valores para asignar a freq
    D = Dia  M = Mes  Y = Año   H = Hora  MIN = Minuto
"""

import pandas as pd 

            # Manejamos un string en formato AAAAMMDD
fechas = pd.Series(pd.date_range('20250101', periods=6, freq='D'))
print(fechas)

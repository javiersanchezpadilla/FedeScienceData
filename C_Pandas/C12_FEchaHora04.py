""" Modificar la frecuencia de afectacion de periods por AÑO"""

import pandas as pd 

            # Manejamos un string en formato AAAAMMDD
fechas = pd.Series(pd.date_range('20250101', periods=6, freq='Y'))
print(fechas)

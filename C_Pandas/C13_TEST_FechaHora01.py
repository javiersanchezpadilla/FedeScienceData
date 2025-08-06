""" Crea una serie temporal que represente todos los días desde el inicio 
    del año 2025 hasta el septimo dia del mismo mes y año. Usa el método 
    adecuado para generar esta serie y asígnala a una variable llamada 
    primera_semana_2025
"""

import pandas as pd 

primera_semana_2025 = pd.Series(pd.date_range('20250101',  periods=7))
print(primera_semana_2025)

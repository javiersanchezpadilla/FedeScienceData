""" El objetivo de estos programas es aprender el
    uso del manejo de las fechas y las horas.
    Pandas nos ofrece datos especiales para el manejo
    de las fechas y las horas, no son string ni integer
    
    pandas.Series(pandas.date_range('AAAAMMDD', periods=dias))

    periods por defeto afecta de un dia en un dia
    """

import pandas as pd 

            # Manejamos un string en formato AAAAMMDD
fechas = pd.Series(pd.date_range('20250101', periods=6))
print(fechas)

print('Imprimimos el tipo de dato de un elemento de la serie')
print(type(fechas[0]))

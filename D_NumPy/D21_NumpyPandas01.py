""" El objetivo de este programa es la conversion de
    estructuras entre NumPy y Pandas.
    conversión de data frames de pandas a 
    array de Numpy
    
    CONVERSION DE DATA FRAME A ARRAR MEDIANTE:
    Atributo        DataFrame.VALUES
    Método          DataFrame.TO_NUMPY()

    El resultado es exactamente el mismo
    """

import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 
            'Impares' : [1, 3, 5], 
            'Pares'   : [2, 4, 6]})

print('\nEl data frame a trabajar es: \n', df)

# Convertimos el data frame a un array mediante el atributo
#               dataFrame.values
array_np1 = df.values
print('\nData Frame convertido mediante el atributo VALUES:\n', array_np1)


# Convertimos el data frame a un array mediante el método
#               dataFrame.to_numpy()
array_np2 = df.to_numpy()
print('\nData Frame convertido mediante el métido TO_NUMPY( ):\n', array_np2)


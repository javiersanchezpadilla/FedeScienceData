""" Manejo de concatenacion
        AXIS=1, concatena por columnas.
        AXIS=0, concatena por filas
"""

import numpy as np 

a = [[1, 2], 
     [3, 4]]

b = [[5, 6], 
     [7, 8]]

# Concatenado por columnas AXIS=1
concatenado_axis_1 = np.concatenate([a, b], axis=1)
print(concatenado_axis_1)
                                    # [[1 2 5 6]
                                    #  [3 4 7 8]]

# Concatenado por filas AXIS=0
concatenado_axis_0 = np.concatenate([a, b], axis=0)
print(concatenado_axis_0)
                                    # [[1 2]
                                    #  [3 4]
                                    #  [5 6]
                                    #  [7 8]]

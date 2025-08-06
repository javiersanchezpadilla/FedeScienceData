""" Operaciones con arrays
    Concatenacion concanate"""

import numpy as np 

x = [1, 2, 3]
y = [1, 2, 3]
z = [1, 2, 3]

array_concatenado = np.concatenate([x, y, z])
print(array_concatenado)
# Resultado esperado [1 2 3 1 2 3 1 2 3]

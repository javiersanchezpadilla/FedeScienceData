""" Funciones universales parte II
    NumPy.LOG(array)    Calculo del logaritmo 
                        BASE 2 y BASE 10"""

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print('Matriz A -->', a)
print('Matriz B -->', b)

log_Base_2_A  = np.log2(a)
log_Base_10_B = np.log10(b)

print('\nEl Logaritmo base 2  de la matriz A es \n', log_Base_2_A)
print('\nEl Logaritmo base 10 de la matriz B es \n', log_Base_10_B)

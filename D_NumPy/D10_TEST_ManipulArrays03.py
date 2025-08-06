""" Crea un array bidimensional A de forma 2x2 que contenga 
    los números del 1 al 4.
    Crea otro array bidimensional B de la misma forma que 
    contenga los números del 5 al 8.

    Realiza las siguientes operaciones e imprime los resultados:

    * La suma de A y B. Almacena el resultado en una variable 
      llamada suma_AB
    * El producto elemento a elemento de A y B. Almacena el 
      resultado en una variable llamada productoAB
"""

import numpy as np 

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

suma_AB = A + B
productoAB = A * B

print('Array A\n', A)
print('\nArray B\n', B)
print('\nSuma de A + B\n', suma_AB)
print('\nEl producto de A * B\n', productoAB)

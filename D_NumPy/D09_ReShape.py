""" En este ejemplo mostrare que podemos hacer operaciones
    con los arrays, podemos hacer cualquier operación
    La unica que causa conflicto es la raiz cuadrada
    la cual se ve al final con 
    NUMPY.SQRT( ) """

import numpy as np 

a = [ [1, 2], [3, 4] ]
b = [ [5, 6], [7, 8] ]

concatenado_axis_1 = np.concatenate([a, b], axis=1)

print('Arrays concatenados\n', concatenado_axis_1)

# Suma de arrays
array_sumado = concatenado_axis_1 + concatenado_axis_1
print('\nArrays sumado consigo mismo\n', array_sumado)

# Producto de arrays
array_multiplicado = concatenado_axis_1 * concatenado_axis_1
print('\nArrays multiplicado consigo mismo\n', array_multiplicado)

# Resta de arrays
array_restado = array_multiplicado - concatenado_axis_1
print('\nArrays restado \n', array_restado)

# Obtenemos la raiz cuadrada de los multiplcados por si mismo
raices = np.sqrt(array_multiplicado)
print('\nArrays raiz cuadradra de array multiplicado \n', raices)

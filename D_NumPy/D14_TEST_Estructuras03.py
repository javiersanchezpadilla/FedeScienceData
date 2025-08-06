"""" Crea un array de 2 dimensiones array_original de forma 
    (2, 3) que contenga los primeros 6 números enteros positivos. 
    Identico al del ejercicio anterior. Luego, crea una copia 
    aplanada de este array y almacénalo en una variable llamada 
    array_aplanado."""

import numpy as np 

array_original = np.array([[1, 2, 3],
                           [4, 5, 6]])

array_aplanado = array_original.flatten()

print('El array original es:\n', array_original)
print('\nEl array aplanado es: \n', array_aplanado)

""" Crea un array de NumPy llamado array_original  que 
    contenga los números del 1 al 12 y luego cambia su forma 
    para que se convierta en un array de 3 filas y 4 columnas. 
    Almacenalo en una variable llamada array_reshape
"""
import numpy as np 

array_original = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array_reshape = array_original.reshape(3, 4)

print('El array original es: ', array_original)
print('El array convertido a dos dimensiones es:\n', array_reshape)

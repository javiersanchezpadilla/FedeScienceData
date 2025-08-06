""" Aplicar operaciones de NumPy sobre los 
    data frame de Pandas."""

import pandas
import numpy

data_frame_pandas = pandas.DataFrame({ 
                        'Impares' : [1, 3, 5], 
                        'Pares'   : [2, 4, 6]})

print('\nEl data frame a trabajar es: \n', data_frame_pandas)

# APLICAMOS OPERACIONES DE NUMPY SOBRE DATA FRAMES DE PANDAS

print('La raiz de los elementos del data frame:')
print(numpy.sqrt(data_frame_pandas))

print('El valor máximo de los elementos del data frame')
print(numpy.max(data_frame_pandas))

print('El valor mínimo de los elementos del data frame')
print(numpy.min(data_frame_pandas))


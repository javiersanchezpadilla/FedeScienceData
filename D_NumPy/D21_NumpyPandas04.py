""" Conversion de arrays de numpy a data frames de pandas.
    Asignado nombres adecuados a las columnas
    
    Los Arrays de numpy no manejan textos, por lo que al convertir 
    le asigna un nombre de columna que es un número."""

import numpy 
import pandas

array_de_numpy = numpy.array([[1, 2], [3, 4], [5, 6]])
print('Mi arreglo de numpy es:\n', array_de_numpy)

data_frame_desde_array_numpy = pandas.DataFrame(array_de_numpy, columns=['Col.1', 'Col.2'])

print('Mi data frame obtenido a partir del array es:')
print(data_frame_desde_array_numpy)

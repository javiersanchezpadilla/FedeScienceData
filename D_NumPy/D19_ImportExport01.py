""" En este programa IMPORTAREMOS un archivo CSV, sin embargo
    debemos tener presente que no es un data frame, como en 
    pandas, por lo que si lo intentamos obtendremos un error,
    es necesario trabajar mas el proceso de importación hacia
    un array."""

import numpy as np 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/medallasNP.csv'

# INTENTO 1
# array = np.genfromtxt(ruta)
# De esta forma nos marca errores 


# INTENTO 2
# array = np.genfromtxt(ruta, delimiter=',')
# Ahora lee el archivo pero marca muchos errores NaN
# [[ nan  nan  nan  nan  nan]
#  [ nan   1.   2.   3.  nan]
#  [ nan   2.   2.   4.  nan]
#  [ 17.   7.  22.  46.  nan]


# INTENTO 3
# array = np.genfromtxt(ruta, delimiter=',', filling_values=0)
# Ya no hay espacios identificados como valores NaN, ya son
# valores cero, el encabezado al ser cero lo marca como cero
# [[  0.   0.   0.   0.   0.]
#  [  0.   1.   2.   3.   0.]
#  [  0.   2.   2.   4.   0.]
#  [ 17.   7.  22.  46.   0.]


# INTENTO 4
# array = np.genfromtxt(ruta, delimiter=',', filling_values=0, skip_header=1)
# En esta version evitamos que se cargara la primer linea, skip_header, le 
# indica a python cuantas lineas debe ignorar desde el inicio del archivo
# [[  0.   1.   2.   3.   0.]
#  [  0.   2.   2.   4.   0.]
#  [ 17.   7.  22.  46.   0.]
#  [  1.   1.   5.   7.   0.]


# INTENTO FINAL Y EL QUE MEJOR SE AJUTA AL TIPO DE ARCHIVO.
array = np.genfromtxt(ruta, delimiter=',', filling_values=0, skip_header=1, dtype=int)
# [[  0   1   2   3   0]
#  [  0   2   2   4   0]
#  [ 17   7  22  46   0]
#  [  1   1   5   7   0]

print(array)

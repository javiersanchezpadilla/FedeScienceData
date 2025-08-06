""" En este ejemplo vamos a valorar cual es mas rápido
    un array o una lista.
    Para ello crearemos una lista y un array con un millon
    de elementos de los cuales elevaremos cada elemento al
    cuadrado y mediremos el tiempo de ejcución"""

import numpy as np 
import time

lista_grande = list(range(1000000))
print(type(lista_grande))

array_grande = np.array(lista_grande)
print(type(array_grande))

# Medimos el tiempo para una lista
inicio_lista = time.time()
for i in lista_grande:
    i ** 2

fin_lista = time.time()
print('La ejecución de la lista fue:', fin_lista - inicio_lista)

# Ahora medimos el tiempo para un array
inicio_array = time.time()
array_grande ** 2

fin_array = time.time()
print('La ejecución del array fue:', fin_array - inicio_array)

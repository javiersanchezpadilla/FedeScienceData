""" slicing."""

import numpy as np 

array1d = np.array([1, 2, 3, 4, 5])
array2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(array1d)
# slicing, imprimit del segundo elemento hasta el cuarto 
# recordar que el 4 no es inclusivo
print(array1d[1:4])

# en arrays de dos dimensiones funciona distinto
print('\n')
print(array2d)
print('Imprimir la fila dos completa', array2d[1, :])
print('Imprimir de la fila 2 los dos ultimos valores', array2d[1, 1:3])

# obtener una columna completa de 2 dimensiones2,5,8
print('obtener los valores medios de todas las filas', array2d[:, 1])

# obtener los dos primeros numeros de las dos primeras filas
print('Obtener los dos primeros valores de las dos primeras filas')
print(array2d[0:2,0:2])
print('\notra forma de los mismo')
print(array2d[:2,:2])

# indexación boleana
# identificar de array1d valores mayores a 3
print('En indexación boleana despues de una condicion regresa')
print('todo el array pero con su valoración boleana a cada valor')
print(array1d > 3)

# indexación boleana para arrays de 2 dimensiones
# buscar que valores dentro del array son pares
print('\nIdentificar que valores son pares en el array de 2 dimensiones')
print(array2d % 2 == 0)
      
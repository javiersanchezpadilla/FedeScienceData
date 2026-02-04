mi_lista = []
print(type(mi_lista))

frutas = ["manzana", "pera", "melon", "sandia"]
print(type(frutas))
print('Impresion de la lista frutas: ',frutas)

print('\nAccede al elemento 0:', frutas[0])    # Acceder a los miembros de una lista
print('Accede al elemento 1', frutas[1])
print('Accede al elemento 2:', frutas[2])

print('\nCambiamos el elemento 2 por piña')
print(frutas)       # Como cambiar los elementos de una lista
frutas[2] = 'piña'
print(frutas)

print('\nAgregamos un nuevo elemento al final de la lista')
print(frutas)       # Agregar una fruta al final de la lista
frutas.append('uvas')
print(frutas)

print('\nAgregaremos en el elemento 0 una fruta')
print(frutas)       # Agregar una fruta en un indice
frutas.insert(0,'naranja')
print(frutas)

print('\nEliminamos una fruta de un índice eliminaremos piña')
print(frutas)       # Eliminar una fruta en un indice
frutas.remove('piña')
print(frutas)

print('\nImprimimos un tipo de lista mas complejo')
mis_listas = [[1, 2, 3, 4], ['a', 'b'], ['Pablo', 'Jorge', 'Sara'], [1.2, 3.1416, 8.99]]
print(type(mis_listas))
print(mis_listas)               # Muestra toda la lista
print('Muestra el elemento 2 de la lista:', mis_listas[2])            # Muetra una elemento de la lista
print('Muestra el elemento dos y su segundo elemento', mis_listas[2][2])         # Muestra un elemento dentro de la sublista
mis_listas[2].append('Wendy')   # agrega al FINAL DE UNA SUBLISTA
print('Agregamos a la sublista 2 el elemento Wendy')
print(mis_listas)

print('\nCambiamos pablo por joaquin')
mis_listas[2][0] = 'Joaquin'    # cambiar Pablo por Joaquin
print(mis_listas)
print(mis_listas[2])
print(mis_listas[2][2])

print('\nPodemos realizaar SLICING')
print(frutas)
print(frutas[1:3])
print(frutas[::2])
print(frutas[::-1])

print('\nPodemos ordenar la lista ya que es mutable')
frutas.sort()               # Ordena la lista
print(frutas)

print('Otro ejemplo de ordenamiento de listas')
lista_numeros = [ 3, 4, 7, 1,  12, 9, -1]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)

print('\nOrdenamiento invertido de la "Z" a la "A"')
lista_numeros.sort(reverse=True)
print(lista_numeros)

print('\”Podemos sumar los contenidos de las listas')
nueva_lista = frutas + mis_listas + lista_numeros
print(type(nueva_lista))
print(nueva_lista)

print('\nPodemos tener listas combinadas (listas), tuplas, etc')
lista_combinada = [[1, 2, 3], ("a", "b", "c"), [[1, 2], (100, 200, 300, 200)] ]
print(lista_combinada)

# desempaquetando la lista
print('DEsempaquetando la lista')
print(lista_numeros)
# desempaquetando todos los elementos uno a uno
a, b, c, d, e, f ,g = lista_numeros
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# deempaquetando solo el primer elemento
print('Desempaquetando solo el primer elemento')
a, *_ = lista_numeros
print(a)
print(_)

# desempaquetando solo el primer y el último elemento
print('Desempaquetando el primero y el último elemento de la lista')
a, *_, b = lista_numeros
print(a)
print(_)
print(b)



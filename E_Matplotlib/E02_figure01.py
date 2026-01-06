""" Figure es el lienzo que contiene los graficos, tambien se puede
    mencionar como marco, lienzo  o canvas dondes vamos a representar
    nuestro gráfico, esto es, es el diseño de fondo
    
    figure      Es el cuado como pared donde colgamos nuestros
                cuadros de gráficos
    axes        Es el cuadro colgado en la pared donde representamos
                los graficos (titulos, etiquetas de los ejes, los ejes)

         figure (todo el lienzo o marco o canvas)
    +---------------------------------------------+
    | +----------+  +-----------+  +------------+ |
    | |          |  |           |  |            | |
    | |   axe    |  |           |  |            | |
    | |          |  |           |  |            | |        
    | +----------+  +-----------+  +------------+ |
    +---------------------------------------------+

    Estos elementos ademas puedo capturarlos en variables para despues
    poder manipularlos.

    """

import matplotlib.pyplot as plt 

numeros = [4, 2, 7, 6, 3]

# Modificamos el fondo a naranja
# Definimos un figure de 2 columnas por 2 filas
plt.subplots(nrows=2, ncols=2)

# En realidad la instrucción anterior nos devuelve una tupla
# con dos valores primero el figure y despues el axe
fig, axs = plt.subplots(nrows=2, ncols=2)
print('El valor de fig =', fig, 'el tipo es ', type(fig))
print('El valor de axe')
print(axs)
print('El tipo es', type(axs))

# Al momento de imprimir el valor de la variable "axs", nos devuelve
# El valor de axe
# [[<Axes: > <Axes: >]
#  [<Axes: > <Axes: >]]  <-- Es una rreglo <class 'numpy.ndarray'>
# 
# Es un arreglo de dos dimensiones con dos filas y dos columas
# básicamente es [[axe1, axe2], [axe3, axe4]]

# Si quiero tomar todo el primer o segundo elemento del arreglo
print('El primer elemento del arreglo: ', axs[0])   # [<Axes: > <Axes: >]
print('El segundo elemento del arreglo:', axs[1])   # [<Axes: > <Axes: >]

# PAra tomar los elementos individuales de cada uno de los elementos
print('Elemento 1 del primer elemento del arreglo:', axs[0][0])
print('Elemento 2 del primer elemento del arreglo:', axs[0][1])
print('Elemento 1 del segundo elemento del arreglo:', axs[1][0])
print('Elemento 2 del segundo elemento del arreglo:', axs[1][1])


plt.show()

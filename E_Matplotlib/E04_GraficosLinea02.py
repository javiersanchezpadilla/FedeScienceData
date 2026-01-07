""" Nomenclaturas para Format en plt.plot() 

    plt.plot() tiene un tercer argumento "format" que nos va 
    a permitir determinar estilos de linea y de puntos para
    nuestros gráficos

COLORES:
--------
    Se especifican con letras únicas.
    'b' azul           'm' magenta
    'g' verde          'y' amarillo
    'r' rojo           'k' negro
    'c' cian           'w' blanco

MARCADORES:
-----------
    Indican los puntos de datos en las gráficas. 
    'o' circulos       '+' cruces
    '^' triangulos     'x' equis
        hacia arriba   'd' diamantes
    's' cuadrados      '*' estrellas
    'v' triangulos
        hacia abajo
    
ESTILOS DE LINEA:
-----------------
    Define como se conectan los puntos en la gráfica.
    '-'  linea solida
    '--' linea discontinua
    '-.' linea punto
    ':'  linea punteada

"""

import matplotlib.pyplot as plt 

fig = plt.figure()
axs = plt.axes()
plt.grid()

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 6, 3, 4, 5, 6, 7]

# plot va a tomar toda la información que le pasemos y la va a representar
# ya sea con lineas o marcadores, con el tercer argumento definimos formatos
# "format" que nos va a permitir determinar estilos de linea y de puntos para
# nuestros gráficos
# plt.plot(x, y, "ro-")   # ro- lineas rojas, cirulos en los marcadores y linea continua
plt.plot(x, y, "b*:")   # b*: lineas azul, estrellas en los marcadores y linea punteada
plt.show()
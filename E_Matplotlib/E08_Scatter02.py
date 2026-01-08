""" DIAGRAMAS DE DISPERSIÓN
    La palabra SCATTER significa algo así como desparramar

    np.linspace(0, 10, 30)  va a agenerar un conjunto de datos entre 0 y 10 y
                            dentro de ese rango va a crear 30 valores que 
                            tengan una distancia similar entre ellos.

    Vamos a quitar las lineas y solo vamos a representar los puntos gráficados

    MARCADORES DISPONIBLES:
    ======================
    Indican los puntos de datos en las gráficas. 
    'o' circulos       '+' cruces
    '^' triangulos     'x' equis
        hacia arriba   'd' diamantes
    's' cuadrados      '*' estrellas
    'v' triangulos
        hacia abajo
"""

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 30)
y = np.sin(x)

# Ahora el mismo gráfico pero eliminando las lineas y dejando solo puntos
# recordar que podemos usar el marcador de la linea (es el tercer argumento)
plt.plot(x, y, '*')

plt.show()
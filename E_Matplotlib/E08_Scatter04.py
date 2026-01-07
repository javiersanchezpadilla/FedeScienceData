""" Modificando carácteristicas de nuestro gráfico

    markersize          Modifica el tamaño del marcador
    linewidth           Cambia el grosor de la linea
    markerfacecolor     Cambia el color de la cara del marcador
                        (el contorno seguira siendo del color definido)

    MARCADORES DISPONIBLES:
    ======================
    Indican los puntos de datos en las gráficas. 
    'o' circulos       '+' cruces
    '^' triangulos     'x' equis
        hacia arriba   'd' diamantes
    's' cuadrados      '*' estrellas
    'v' triangulos     'p' pentagonos
        hacia abajo
"""
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 30)
y = np.sin(x)

# Ahora modificamos el color de la linea, el tamaño de los marcadores, 
# tambien el ancho de la linea
plt.plot(x, y, '-p', color='red', markersize=15, linewidth=4)

plt.show()

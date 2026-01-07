""" Creación de graficos tipo scatter con la funcion scatter 
    Al hacer uso de esta funcion que realmente es la especial 
    para definir este tipo de gráfico, es que se habilitan 
    funciones específicas para este tipo de gráfico
    
    c       color
    s       size
    alpha   Transparencia
"""

import random as rand
import matplotlib.pyplot as plt 

for valor in range(100):
    x = rand.random()
    y = rand.random()
    # plt.scatter(x, y)     # crea puntos 
    color = rand.randint(1, 255)
    # plt.scatter(x, y, c=color)                # colores aleatorios para los puntos
    tamanio = rand.randint(1, 500)
    #plt.scatter(x, y, c=color, s=tamanio)      # Cambiando el tamaño de los puntos
                                                # Aumentando transparencia a los puntos
    plt.scatter(x, y, c=color, s=tamanio, alpha=0.3)

plt.colorbar()      # Permite colocar del lado derecho del gráfico una barra de colores

plt.show()


""" SCATTER con todos los tipos de marcadores que podemos usar

    MARCADORES DISPONIBLES:
    ======================
        Indican los puntos de datos en las gráficas. 
        'o' circulos       '+' cruces
        '^' triangulos     'x' equis
            hacia arriba   'd' diamantes
        's' cuadrados      '*' estrellas
        'v' triangulos
            hacia abajo

    Vamos crear un generador de números pseudoaleatorios aislado e 
    independiente, Es la misma solución que el problema anterior per
    con otro estilo
"""

import numpy as np 
import random as ran
import matplotlib.pyplot as plt 

aleatorio = np.random.RandomState(0)
marcadores = ['o', '+', '^', 'x', 'd', 's', '*', 'v']

for marcador in marcadores:
    for cinco_valores in range(5):
        plt.plot(ran.random(), ran.random(), marcador)

plt.show()

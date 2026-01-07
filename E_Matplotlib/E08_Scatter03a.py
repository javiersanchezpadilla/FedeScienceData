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
    independiente, que permita generar secuencias de números aleatorios 
    reproducibles.            
    aleatorio = np.random.RandomState(0)            
"""

import numpy as np 
import matplotlib.pyplot as plt 

aleatorio = np.random.RandomState(0)
marcadores = ['o', '+', '^', 'x', 'd', 's', '*', 'v']

for marcador in marcadores:
    # aquí armamos el gráfico y hasta que está terminado se renderiza
    plt.plot(aleatorio.rand(5), aleatorio.rand(5), marcador)

# aqui una vez terminado el gráfico es que se renderiza
plt.show()

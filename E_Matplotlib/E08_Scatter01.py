""" La palabra SCATTER significa algo así como desparramar

    np.linspace(0, 10, 30)  va a agenerar un conjunto de datos entre 0 y 10 y
                            dentro de ese rango va a crear 30 valores que 
                            tengan una distancia similar entre ellos.
"""

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 30)
y = np.sin(x)

# Realmente lo que hemos creado es un gráfico de lineas
plt.plot(x, y)

plt.show()

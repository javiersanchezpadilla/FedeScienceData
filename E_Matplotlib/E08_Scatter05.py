""" Generando valores aleatorios para entender mejor el uso
    de los gráficos del tipo scatter"""

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 30)
y = np.sin(x)

# Ahora modificamos el color de la linea, el tamaño de los marcadores, 
# tambien el ancho de la linea
plt.scatter(x, y)

plt.show()

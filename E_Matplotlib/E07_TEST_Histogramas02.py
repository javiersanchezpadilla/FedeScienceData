""" Histogramas en Matplotlib

    Utilizando un conjunto de datos generado con numpy, crea un histograma 
    sencillo de 1000 números generados al azar, 
    almacenalos en una variable llamada datos con una distribución normal 
    y crea un histograma con 30 barras (bins). 
    Personaliza el color de las barras a azul y el borde a negro. """

import numpy as np 
import matplotlib.pyplot as plt 

datos = np.random.randn(1000)

plt.hist(datos, bins=30, color='blue', edgecolor='black')
plt.show()

""" Histogramas en Matplotlib

    Utilizando un conjunto de datos generado con numpy, 
    crea un histograma sencillo de 1000 números generados al azar, 
    almacenalos en una variable llamada datos . 
    Siguiendo una distribución normal estándar. """

import numpy as np 
import matplotlib.pyplot as plt 

datos = np.random.randn(1000)
plt.hist(datos)
plt.show()

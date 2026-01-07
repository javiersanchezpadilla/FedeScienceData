""" Histogramas en Matplotlib

    Crea un único gráfico en el que se muestren tres histogramas superpuestos 
    con los siguientes requisitos:

    Genera tres series de datos aleatorios utilizando numpy:

    La primera serie debe contener 1000 valores (x1).
    La segunda serie debe contener 500 valores (x2).
    La tercera serie debe contener 100 valores (x3).

    Todas las series deben seguir una distribución normal.

    Los histogramas deben cumplir con las siguientes especificaciones:
        A) Cada histograma debe contener 40 intervalos (bins).
        B) Deben utilizar el estilo stepfilled para el tipo de histograma (histtype).
        C) Aplica un nivel de transparencia (alpha) de 0.5 a cada histograma para 
           lograr la superposición.

    Utiliza Matplotlib para generar el gráfico.

    Observación:

    El gráfico resultante deberá mostrar tres histogramas superpuestos en diferentes 
    colores, con bordes claros y relleno."""

import numpy as np 
import matplotlib.pyplot as plt 

x1 = np.random.randn(1000)
x2 = np.random.randn(500)
x3 = np.random.randn(100)

plt.hist(x1, bins=40, histtype='stepfilled', alpha=0.5)
plt.hist(x2, bins=40, histtype='stepfilled', alpha=0.5)
plt.hist(x3, bins=40, histtype='stepfilled', alpha=0.5)

plt.show()

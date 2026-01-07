""" SUPERPONIENDO VARIOS HISTOGRAMAS.
    ---------------------------------

    Modificando valores del gráfico del histograma
    Dentro de plt.histo() existen varios argumentos

    bins        Permite definier el número de columnas que tendrá el histograma
    alpha       Nivel de opacidad 0 transparente 1 opaco
    color       Permite definir el número de color para las barras del gráfico
    edgecolor   Color del contorno de cada barra del gráfico
    histtype    Permite definir el relleno de cada barra
                bar         El valor por defecto. Es un histograma tradicional 
                            de barras. Si se proporcionan múltiples conjuntos 
                            de datos, las barras se muestran una al lado de la otra.
                barstacked  Un histograma de barras apiladas, donde varios conjuntos 
                            de datos se apilan uno encima del otro.
                step        Genera un gráfico de líneas que, por defecto, no está 
                            rellenado, mostrando solo el contorno del histograma.
                stepfilled  Similar a 'step', pero el área debajo de la línea está 
                            rellenada. 
"""
import matplotlib.pyplot as plt 
import numpy as np 

# tengo tres conjuntos distintos de numeros aleatorios
x1 = np.random.randn(1000)
x2 = np.random.randn(500)
x3 = np.random.randn(100)

# los quiero representar a todos dentro de un mismo histograma
# Como hay un solo AXE los va a representar a todos en una mismo 
# histograma
plt.hist(x1, histtype='stepfilled', alpha=0.3, bins=40)
plt.hist(x2, histtype='stepfilled', alpha=0.3, bins=40)
plt.hist(x3, histtype='stepfilled', alpha=0.3, bins=40)
plt.grid()

plt.show()

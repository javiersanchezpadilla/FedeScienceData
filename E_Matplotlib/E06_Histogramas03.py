""" Modificando valores del gráfico del histograma

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

#import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

# crea un conjunto de 1000 números aleatorios
numeros = np.random.randn(1000)
print(numeros)

plt.grid()

# creamos el histograma con 40 graficos verticales (40 columnas)
# plt.hist(numeros, bins=40)

# Podemos agregar transparencia a las barras
# plt.hist(numeros, bins=40, alpha=0.5)

# Podemos definir el color de las barras
# plt.hist(numeros, bins=40, alpha=0.5, color='red')

# Definiendo el color del borde de cada barra
# plt.hist(numeros, bins=40, alpha=0.5, color='red', edgecolor='green')

# Solicitando que solo dibuje el contorno del gráfico de las barras
plt.hist(numeros, bins=40, alpha=0.5, color='red', edgecolor='green', histtype='step')

plt.show()

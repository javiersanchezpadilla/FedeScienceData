""" Generar un histograma con valores mas abstractos y uniformes

    Para esto vamos a generar valores aleatorios:
        np.random               Crea valores aleatorios
        np.random.randn()       Cread un conjunto de datos en este caso 1000

    Los valores generados por randn() son valores con una distribución normal 
    estandar (tambien conocida como distribución gaussiana), en esta distribución
    el promedio de todos los números que se generen de manear aleatoria van a 
    tener un valor promedio cercano a cero, ya sea positivos o negativos, y la 
    desviación estandar (cuanto se alejan los demas números va ser un valor 
    cercano al 1 (uno) (entre -1 y 1).
    En el grafico vamos a ver que la mayor parte de los puntos esta en el valor 0
    y el resto delos valores que se alejan (-1, -2, -3, 1, 2, 3) tienden a cero
"""

#import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

# crea un conjunto de 1000 números aleatorios
numeros = np.random.randn(1000)
print(numeros)

plt.hist(numeros)
plt.grid()
plt.show()

""" Ejemplo para entender el alcance de matplotlib
    Creando nuestro primer gráfico

    plt.plot()      Permite crear un gráfico
    plt.show()      Permite mostrar el gráfico
"""

import matplotlib.pyplot as plt

# Creamos un conjunto de datos
numeros = [4, 2, 7, 6, 3]

plt.plot(numeros)
# Al no tener mas valores de referencia se tomará el índice con
# valor de referencia en el eje "x", 
# numeros = [4, 2, 7, 6, 3]
# 4 indice 0     6 índice 3
# 2 indice 1     3 índice 4
# 7 indice 2  

plt.show()

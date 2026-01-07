""" Gráficos Scatter en Matplotlib

    Utilizando los mismos datos del ejercicio anterior:

    # Datos para el gráfico
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    Crea un gráfico scatter con el método scatter() y personalízalo cambiando 
    el color de los puntos a rojo y el tamaño de los puntos a 50. 
    Si tienes dudas con los parámetros a emplear recuerda que puedes buscar 
    en la ayuda del método scatter() .
"""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, color='red', s=50)
plt.show()

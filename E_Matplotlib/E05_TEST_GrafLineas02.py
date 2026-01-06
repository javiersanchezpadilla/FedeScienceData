""" Gráficos de Línea (Line Plots) en Matplotlib

    Utilizando el gráfico de línea simple con las rejillas (o grid) activas. 
    Identico al ejercicio anterior con los siguientes datos:

    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

Agrega los métodos necesarios para que el grafico se muestre con lineas rojas 
sólidas y con círculos en los puntos."""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.grid()
plt.plot(x, y, "ro-")
plt.show()

""" Gráficos de Línea (Line Plots) en Matplotlib

    Utilizando el gráfico de línea simple con las rejillas (o grid) activas, 
    con lineas rojas sólidas y con círculos en los puntos. Identico al ejercicio 
    anterior con los siguientes datos:

    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    Agrega los métodos necesarios para definir los límites del gráfico del 
    eje x mínimo en 0 y máximo en 10, y el eje y mínimo en 0 y máximo en 12"""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.grid()
plt.axis([0, 10, 0, 12])
plt.plot(x, y, "ro-")

plt.show()

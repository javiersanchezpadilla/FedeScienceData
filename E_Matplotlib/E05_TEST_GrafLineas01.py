""" Gráficos de Línea (Line Plots) en Matplotlib

    Crea un gráfico de línea simple utilizando Matplotlib 
    con los siguientes datos:

    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    Debes activar el grid (o parrilla) para ver las líneas de guía 
    que nos ayuden a medir nuestros datos."""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.grid()
plt.plot(x, y)
plt.show()

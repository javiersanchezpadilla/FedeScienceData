""" Definición de los valores máximos y mínimos de nuestro gráfico

    Para definir la escala de los ejes de coordenadas "x", "y"
        plt.axis([x_min, x_max, y_min, y_max])  

    Podemos solicitar ayuda mediante
        help(plt.axis)

    plt.grid() activa y desactiva, esto es, 1 vez lo activa, 2 activa y desativa, etc.
"""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 6, 3, 4, 5, 6, 7]

fig = plt.figure()
axs = plt.axes()
plt.grid()

plt.axis([0, 8, 0, 8])
plt.plot(x, y, "ro-")   

plt.show()      # Renderiza el gráfico

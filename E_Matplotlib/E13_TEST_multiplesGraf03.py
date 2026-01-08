""" Creación de Múltiples Gráficos con Matplotlib

    Personaliza los dos subgráficos del Ejercicio 2

    Emplea los mismo datos:

        x = [1, 2, 3, 4] 
        y = [2, 4, 8, 16]

    Agregando títulos diferentes a cada gráfico, cambiando el color 
    de las líneas gráfica scatter. Asegúrate de que cada elemento 
    de personalización se aplique correctamente al subplot 
    correspondiente de la forma siguiente:

        Gráfico 1 (Izquierda):              Gráfico 2 (Derecha):
        Titulo: Gráfico de línea            Titulo: Gráfico de scatter
        Color de línea: verde               Color de simbolos: rojo
"""

import matplotlib.pyplot as plt 

fig, axs = plt.subplots(nrows=1, ncols=2)

ax1 = axs[0]
ax2 = axs[1]

ax1.plot([1, 2, 3, 4], [2, 4, 8, 16], color='green')
ax2.scatter([1, 2, 3, 4], [2, 4, 8, 16], color='red')

ax1.set_title('Gráfico de línea')
ax2.set_title('Gráfico de scatter')

plt.show()

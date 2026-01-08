""" Creación de Múltiples Gráficos con Matplotlib

    Utilizando la figura y los subgráficos creados en el Ejercicio 1
    Dibuja un gráfico de línea en el primer subplot (izquierdo) 
    con los datos siguientes [1, 2, 3, 4], [2, 4, 8, 16]

    Y otro gráfico scatter (derecho) en el segundo subplot. 
    con los datos siguientes [1, 2, 3, 4], [2, 4, 8, 16]
"""

import matplotlib.pyplot as plt 

fig, axs = plt.subplots(nrows=1, ncols=2)

ax1 = axs[0].plot([1, 2, 3, 4], [2, 4, 8, 16])
ax2 = axs[1].scatter([1, 2, 3, 4], [2, 4, 8, 16])

plt.show()

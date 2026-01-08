""" Creación de Múltiples Gráficos con Matplotlib

    Crea una figura en Matplotlib que contenga dos subgráficos 
    (uno al lado del otro) utilizando la función subplots. 
    Asegúrate de que cada subplot quede guardado como un objeto 
    diferente para poder manipularlos después. 
    No necesitas agregar ningún dato a los gráficos en este ejercicio."""

import matplotlib.pyplot as plt 

fig, axs = plt.subplots(nrows=1, ncols=2)
ax1 = axs[0]
ax2 = axs[1]


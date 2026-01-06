""" Ejemplo para entender el alcance de matplotlib

    plt.plot()      Permite crear un gráfico
    plt.show()      Permite mostrar el gráfico
    plt.savefig()   Permite guerdar el gráfico en el 
                    formato que deseemos

"""

import matplotlib.pyplot as plt

ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/graficos/uno.jpg'
# Creamos un conjunto de datos
numeros = [4, 2, 7, 6, 3]

plt.plot(numeros)
plt.savefig(ruta)

plt.show()

""" Importar un data frame y mostrarlo en forma de grafica

    Como los textos en el eje "x" van a estar muy pegados podemos
    modificarlos mediante la propiedad
        plt.xticks(rotation=45)
"""

import pandas as pd 
import matplotlib.pyplot as plt 


ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/graficos/Lluvias_region_A.csv'

df = pd.read_csv(ruta)
print(df.info())

plt.figure(facecolor='gray')

plt.plot(df['region'], df['enero'], "c*-")
plt.xticks(rotation=45)
plt.grid()

plt.show()

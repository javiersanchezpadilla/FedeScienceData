""" Graficos del tipo histograma, nos permite mostrar la distribución
    de nuestros valores, pertenece a la clasificacion de distribuciones
    estaditicas, básicamente es un gráfico que nos muestra con que
    frecuencia se repiten los valores de nuestros registros, esto quiere decir
    que una barra muy alta significa que los valores en nuestros registros se
    repite muchas veces
    
    Para crear un histograma usamos una funciona llamada, la cual solo requiere
    una secuencia de valores de "x", el eje "y" estará formado o definido por el
    número de repeticiones de cada elemento del eje "x"

    plt.hist()
    """

import matplotlib.pyplot as plt 
import pandas as pd

ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/graficos/Ventas.csv'

df = pd.read_csv(ruta)
print(df.info())

# Vamos a crear un histograma de la seria Producto
# recordemos que la altura de las barras va a depeneder
# de cuantas veces se repita el valor en la serie de datos
plt.hist(df['Producto'])
plt.show()

""" Como construir cualquier tipo de gráfico en Matplotlib

    El archivo muestra la intensidad luminica del mapa
    en una ciudad ficticia

    Para elegir el tipo de gráfico vamos a la página oficial
    https://matplotlib.org/stable/plot_types/index.html

    El ejemplo puede interpretarse como que nos han pasado las 
    mediciones para ver que tan intesa se ve la luz en cada punto
    de la ciudad y lo que se requiere es un gráfico que permita
    entender estos datos
    
    Vamos a elegir el tipo de gráfico hexbin(x, y, C) y con base a 
    su ayuda vamos a armar el gráfico
    """

import pandas as pd 
import matplotlib.pyplot as plt 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData\
/Z_ArchivosExternos/graficos/Iluminacion.csv'

df = pd.read_csv(ruta)
print(df.head())

fig, ax = plt.subplots()

# Le asignamos un nombre al gráfico
plt.title('Luminosidad en villa luz')

# Esta es la primer version de la creación del gráfico sin ser asignado 
# a una variable

# ax.hexbin(df['Latitud'],            # valor en eje "x"
#           df['Longitud'],           # valor en eje "y"
#           C=df['Luminosidad'],      # valor a representar
#           gridsize=50,              # tamaño del gráfico
#           cmap='Greens')            # mapa de colores basado en gamas en tonos color verde

# Versión 2 (despues de plt.colorbar()) 
# Ahora fue asignado a una variable mapeable para poder crear la barra lateral
hb = ax.hexbin( df['Latitud'],              # valor en eje "x"
                df['Longitud'],             # valor en eje "y"
                C=df['Luminosidad'],        # valor a representar
                gridsize=50,                # tamaño del gráfico
                cmap='Greens')              # mapa de colores basado en gamas en tonos color verde


# Asignamos un color de fondo al gráfico
ax.set_facecolor('#000000')

# Agregamos una barra lateral de colores, 
# como pide una variable escalar asignamos el gráfico a una variable
plt.colorbar(hb,                            # variable escalar del gráfico
             label='Nivel de sombras')      # etiqueta de la barra lateral

# Agregamos etiquetas a los ejes
plt.xlabel('Latitud')
plt.ylabel('Longitud')

plt.show()

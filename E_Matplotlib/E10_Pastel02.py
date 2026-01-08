""" Graficos de pastel PIE PLOT

    Aumentando como parte del grafico las etiquetas de cada rebanada del pasterl

    plt.pie()   Solo pide una sola secuencia de valores (los valores de "x")
    labels      Definir una lista con los valores de las etiquetas a mostrar
"""

import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame({'etiquetas' : ['Manzanas', 'Platanos', 'Naranjas', 'Uvas'],
                   'cantidad' : [30, 60, 80, 20]})

# PAra aumentar las etiquetas de las frutas
plt.pie(df['cantidad'], 
           labels=df['etiquetas'])

plt.show()

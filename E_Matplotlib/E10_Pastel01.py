""" Graficos de pastel PIE PLOT

    plt.pie()   Solo pide una sola secuencia de valores (los valores de "x")
"""

import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame({'etiquetas' : ['Manzanas', 'Platanos', 'Naranjas', 'Uvas'],
                   'cantidad' : [30, 60, 80, 20]})

# PAra visualizar el grafico simple
plt.pie(df['cantidad'])

plt.show()

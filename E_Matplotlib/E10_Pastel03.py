""" Graficos de pastel PIE PLOT

    Aumentando como parte del grafico los valores en porcentaje correspondiente
    a cada una de las rebanadas

    plt.pie()           Solo pide una sola secuencia de valores (los valores de "x")
    labels              Definir una lista con los valores de las etiquetas a mostrar
    autopct='%1.4f%%'   auto porcentaje el formato es '%1.1f%%'
                        1) '%1.1f%%' Debe iniciar y finalizaar con el simbolo de 
                           porcentaje % %
                        2) el 1.1 significa un entero un punto y un solo decimal, 
                           1.2 un entero y dos decimales, 1.4 un entero y cuatro decimales
                        3) 'f' es un numero flotante y por último el simbolo de porcentaje 
                           solo es para que aparezca como simbolo
"""

import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame({'etiquetas' : ['Manzanas', 'Platanos', 'Naranjas', 'Uvas'],
                   'cantidad' : [30, 60, 80, 20]})

# Ahora queremos ver el porcentaje que representa cada fruta
# autopct (auto porcentaje) el formato es '%1.1f%%'
plt.pie(df['cantidad'],                # Se representa solo el eje "x"
        labels=df['etiquetas'],        # Se asignan las etiquetas al gráfico
        autopct='%1.4f%%')             # se formatean las etiquetas de los valores

plt.show()

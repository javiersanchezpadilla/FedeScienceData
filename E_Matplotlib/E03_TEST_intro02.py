""" Modifica la apariencia de tu gráfico cambiando el color de fondo 
    de la figura a verde. Utiliza la misma serie de números del ejercicio 
    anterior: [10, 15, 7, 10, 22]

    Almacena el gráfico en una variable llamada grafico_verde_numeros"""

import matplotlib.pyplot as plt 

numeros = [10, 15, 7, 10, 22]

plt.figure(facecolor='green')
grafico_verde_numeros = plt.plot(numeros)

plt.show()

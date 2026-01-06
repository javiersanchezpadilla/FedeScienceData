""" Crea un gráfico de líneas simple usando Matplotlib para visualizar la 
    siguiente serie de numeros: [10, 15, 7, 10, 22]

    Almacena el gráfico en una variable llamada grafico_numeros"""

import matplotlib.pyplot as plt 

numeros = [10, 15, 7, 10, 22]
grafico_numeros = plt.plot(numeros)
plt.show()

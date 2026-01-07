""" Gráficos Scatter en Matplotlib

    Crea un gráfico scatter simple usando Matplotlib para visualizar la 
    relación entre dos listas de datos: 
    x = [1, 2, 3, 4, 5] 
    y = [2, 3, 5, 7, 11]
    
    Utiliza el método scatter() para generar el gráfico.
"""

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11]

plt.scatter(x, y)
plt.show()


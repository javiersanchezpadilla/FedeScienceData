""" Gráficos Scatter en Matplotlib

    Genera un gráfico scatter que muestre dos series de datos.

    Para la primera serie utiliza:
    ------------------------------
        Color: azul     Marcador: 'o'   Etiqueta: Serie 1
        x1 = [1, 2, 3, 4, 5] 
        y1 = [2, 3, 5, 7, 11] 

    Para la segunda serie emplea:
    -----------------------------
        Color: verde        Marcador: '^'   Etiqueta: Serie 2
        x2 = [1, 2, 3, 4, 5] 
        y2 = [1, 4, 9, 16, 25] 

    Proporciona una leyenda para identificar cada serie.
    Si tienes dudas con los parámetros a emplear recuerda que puedes buscar en 
    la ayuda del método scatter()"""

import matplotlib.pyplot as plt 

# Datos de la serie 1
x1 = [1, 2, 3, 4, 5] 
y1 = [2, 3, 5, 7, 11] 

# Datos de la serie 2
x2 = [1, 2, 3, 4, 5] 
y2 = [1, 4, 9, 16, 25] 

plt.scatter(x1, y1, color='blue', marker='o', label='Serie 1')
plt.scatter(x2, y2, color='green', marker='^', label='Serie 2')

plt.legend()
plt.show()

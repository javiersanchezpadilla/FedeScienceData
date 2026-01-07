""" Gráficos Scatter en Matplotlib

    Genera un gráfico scatter que muestre dos series de datos.

    Para la primera serie utiliza:
    ------------------------------
        Color: azul     Marcador: 'o'   Etiqueta: Serie x²
        x1 = np.arange(1, 6)
        y1 = x1**2

    Para la segunda serie emplea:
    -----------------------------
        Color: verde        Marcador: '^'   Etiqueta: Serie x³
        x2 = np.arange(1, 6)
        y2 = x2**3 

    Proporciona una leyenda para identificar cada serie.
    Proporciona una leyenda para cada uno de los ejes de coordenadas
"""



import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo para dos series
x1 = np.arange(1, 6)
y1 = x1**2
x2 = np.arange(1, 6)
y2 = x2**3

# Crear el gráfico de dispersión para la primera serie con una etiqueta
plt.scatter(x1, y1, label='Serie x²')

# Crear el gráfico de dispersión para la segunda serie con otra etiqueta y un marcador diferente
plt.scatter(x2, y2, label='Serie x³', marker='^', color='r')

# Añadir etiquetas a los ejes y un título (opcional)
plt.xlabel('Este es el Eje X')
plt.ylabel('Este es el Eje Y')
plt.title('Gráfico de Dispersión con Leyendas')

# Mostrar la leyenda. Matplotlib usa automáticamente las etiquetas asignadas
plt.legend()

# Mostrar el gráfico
plt.show()

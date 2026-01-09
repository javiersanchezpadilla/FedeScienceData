""" Crea Cualquier tipo de Gráficos desde Matplotlib

    Investiga en la documentación de Matplotlib y crea un gráfico de tallo (stem):
    https://matplotlib.org/stable/plot_types/index.html
    https://matplotlib.org/stable/plot_types/3D/stem3d.html 

    Gráfico stem
    Que represente la relación entre dos conjuntos de datos "x" e "y".
    Los valores para "x" deben ser los números enteros del 1 al 10, 
    y los valores para "y" deben ser el cuadrado de cada número en x.

    Asegúrate de incluir títulos adecuados para el gráfico, así como para los ejes x e y.
        Título del gráfico: "Relación entre Números y sus Cuadrados"
        Título del eje x: "Número (x)"
        Título del eje y: "Cuadrado del número (x^2)"
"""
import matplotlib.pyplot as plt 
import numpy as np

x = [x for x in range(1, 11)]
y = [x ** 2 for x in range(1, 11)]

plt.title("Relación entre Números y sus Cuadrados")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.stem(x, y)


ax.show()

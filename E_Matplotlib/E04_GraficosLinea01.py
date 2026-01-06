""" Tambien podemos crear la figuras y los axes de forma
    individual
    
    plt.grid()      Permite dibujar el grill o parrilla
    """


import pandas as pd 
import matplotlib.pyplot as plt 

fig = plt.figure()
axs = plt.axes()
plt.grid()

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 6, 3, 4, 5, 6, 7]

# plot va a tomar toda la información que le pasemos y la va a representar
# ya sea con lineas o marcadores
plt.plot(x, y)
plt.show()

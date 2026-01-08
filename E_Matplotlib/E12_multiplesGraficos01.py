""" Vamos a usar variables para controlar los gráficos a mostrar

    En este ejemplo se generar dos ejes, uno para cada uno de los
    gráficos
    
    +----------------------------------------+
    | +----------------+ +-----------------+ |
    | |                | |                 | |
    | |                | |                 | |
    | |      ax1       | |       ax2       | |  figure (fig)
    | |                | |                 | |
    | |                | |                 | |
    | |                | |                 | |
    | +----------------+ +-----------------+ |
    +----------------------------------------+
    """

import matplotlib.pyplot as plt 
# %matplotlib inline

fig, axs = plt.subplots(ncols=2, nrows=1)
ax1 = axs[0]
ax2 = axs[1]

print(type(fig))    # <class 'matplotlib.figure.Figure'>
print(type(ax1))    # <class 'matplotlib.axes._axes.Axes'>
print(type(ax2))    # <class 'matplotlib.axes._axes.Axes'>

plt.show()

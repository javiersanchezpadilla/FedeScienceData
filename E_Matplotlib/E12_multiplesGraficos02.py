"""

"""

import matplotlib.pyplot as plt 
# %matplotlib inline

fig, axs = plt.subplots(ncols=2, nrows=1)
ax1 = axs[0]
ax2 = axs[1]

ax1.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax2.scatter([1, 2, 3, 4], [1, 4, 9, 16])

ax1.set_title('Gráfico de linea')
ax2.set_title('Gráfico Scatter (dispersión)')

plt.show()

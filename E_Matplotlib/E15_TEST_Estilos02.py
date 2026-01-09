""" Estilo para tus Gráficos con Matplotlib

    Utiliza el gráfico de barra del anterior empleando los mismos datos:

        df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20] })

    Asegurate de que en el eje X se muestren las frutas, 
    y en el eje Y se muestren las cantidades.

    Añade al gráfico, el siguiente título: 'Distribución de frutas en el almacén'
    Como nuevo requerimiento debes emplear el estilo: 'ggplot'.
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({"frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                   "cantidades": [40, 25, 15, 20] })

# Definimos el estilo del gráfico
plt.style.use('ggplot')

plt.bar(df['frutas'], df['cantidades'])
plt.title('Distribución de frutas en el almacén')

# REnderizamos el gráfico
plt.show()

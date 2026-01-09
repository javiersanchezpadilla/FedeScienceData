""" Estilo para tus Gráficos con Matplotlib 

    Basado en los datos de frutas y ventas que hemos venido trabajando en 
    los dos ejercicios anteriores:

        df = pd.DataFrame({ "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                            "cantidades": [40, 25, 15, 20] })

    Crea un gráfico de pastel que muestre la distribución de frutas en el almacén
    El gráfico de pastel debe incluir etiquetas que identifiquen cada tipo de fruta.
    Además, usa el parámetro correcto para mostrar el porcentaje de cada fruta en el 
    gráfico en el siguiente formato:

    Tipo float.
    Un solo decimal después de la coma
    Coloca el simbolo de % al final
    Separa todas las poriciones, es decir explotalas todas para que se vean separadas.
    Añade al gráfico el siguiente título: 'Distribución de frutas en el almacén'
    Finalmente agrega el estilo "dark_background" a tu gráfico.
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({ "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                    "cantidades": [40, 25, 15, 20] })

plt.style.use("dark_background")

plt.pie(df['cantidades'], 
           labels=df['frutas'], 
           autopct='%1.1f%%',
           explode=(0.1, 0.1, 0.1, 0.1))
plt.title('Distribución de frutas en el almacén')
plt.show()

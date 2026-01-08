""" Gráfico Pastel (Pie Plot) con Matplotlib 

    Tomando el dataframe que hemos empleado en los ejercicios anteriores:

        df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20]
        })

    Manten las configuraciones que hemos realizado en el ejercicio 2
    Gráfico Pastel (Pie Plot) con Matplotlib 2

    Mejora aún más tu gráfico de pastel realizando los siguientes pasos:

    1) Asigna un color específico a cada fruta usando la lista de colores siguientes:
       colors = ['red', 'yellow', 'darkred', 'orange']

    2) No modifiques la lista ni su nombre.
    3) Agrega una sombra.
    4) Separa la porción de las Cerezas del resto de las frutas en el gráfico.
    5) Finalmente, añade al gráfico, el siguiente título:  
    'Distribución de frutas en el almacén'

    Recuerda importar los módulos de python necesarios para que tu código funcione correctamente.
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({"frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                   "cantidades": [40, 25, 15, 20]})


plt.pie(df['cantidades'], 
        labels=df['frutas'], 
        autopct='%1.1f%%',
        colors = ['red', 'yellow', 'darkred', 'orange'],
        shadow=True,
        explode=(0, 0, 0.1, 0))

plt.title('Distribución de frutas en el almacén')

plt.show()

""" Gráfico Pastel (Pie Plot) con Matplotlib 

    Crea un gráfico de pastel que muestre la distribución de los siguientes tipos de 
    frutas en un almacén: 
    
    Manzanas (40), Bananas (25), Cerezas (15) y Duraznos (20).

    Para ello puedes emplear el dataframe que ya viene proporcionado en este ejercicio.

        df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20]
        })

    Utiliza la función adecuada de Matplotlib para realizar esta tarea.
    Recuerda importar los módulos de python necesarios para que tu código funcione 
    correctamente."""

import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20]
        })

plt.pie(df['cantidades'])
plt.show()

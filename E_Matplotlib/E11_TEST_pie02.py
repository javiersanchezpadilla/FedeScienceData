""" Gráfico Pastel (Pie Plot) con Matplotlib

    Utilizando el mismo conjunto de datos del ejercicio anterior:

        df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20]
        })

    Modifica tu gráfico de pastel para incluir etiquetas que identifiquen 
    cada tipo de fruta.
    Además, usa el parámetro correcto para mostrar el porcentaje de cada 
    fruta en el gráfico en el siguiente formato:

    1) Tipo float  
    2) Un solo decimal   
    3) Coloca el simbolo de % al final

    Recuerda importar los módulos de python necesarios para que tu código funcione correctamente."""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({ "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                    "cantidades": [40, 25, 15, 20]})

plt.pie(df['cantidades'], labels=df['frutas'], autopct='%1.1f%%')
plt.show()

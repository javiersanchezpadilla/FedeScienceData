""" Estilo para tus Gráficos con Matplotlib 

    Crea un gráfico de barras utilizando Matplotlib para visualizar el 
    número de ventas de diferentes tipos de frutas. 
    Utiliza el siguiente conjunto de datos:

        df = pd.DataFrame({
            "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
            "cantidades": [40, 25, 15, 20]})

    Asegurate de que en el eje X se muestren las frutas, y en el eje 
    Y se muestren las cantidades.
    Añade al gráfico, el siguiente título: 'Distribución de frutas en el almacén'
    Observación: No hemos visto en las lecciones anteriores como hacer un gráfico 
    de barras, deberás investigar como hacerlo, para ellos te dejo el enlace a 
    la documentación oficial de Matplotlib

    Documentación oficial de Matplotlib https://matplotlib.org/stable/users/index.html

    Y especificamente a la función bar con la cual podrás crear tu gráfico de barras.
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    """

import matplotlib.pyplot as plt 
import pandas as pd 


df = pd.DataFrame({"frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
                   "cantidades": [40, 25, 15, 20]})

plt.bar(df['frutas'], df['cantidades'])
plt.title('Distribución de frutas en el almacén')

plt.show()

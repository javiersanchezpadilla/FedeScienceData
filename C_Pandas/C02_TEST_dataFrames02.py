""" Dado el DataFrame df con columnas Nombre, Edad y Ciudad, como se mostró 
    en el ejercicio en clase, escribe un código para filtrar las filas que 
    contienen personas de 25 años o más. Asegurate de guardar en el dataframe 
    filtrado en una variable llamada: df_filtrado
"""

import pandas as pd 

data = {
        'Nombre' : ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad' : [25, 30, 22, 27],
        'Ciudad' : ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
df_filtrado = df[df['Edad'] > 24]
print(df_filtrado)

""" Aqui nuevamente tenemos el problema de los índices
            Este es el resultado
            id_producto  Cantidad_vendida  Precio
            0         1001              30.0    20.5
            1         1002               NaN    15.0
            2         1003              25.0     NaN
            3         1003              25.0    22.5
            Data Frame con eliminados
            id_producto  Cantidad_vendida  Precio
            0         1001              30.0    20.5
            3         1003              25.0    22.5

    en el último resultado yo entiendo que el valor de los índices es 0 y 3 
    (del dataframe donde eliminamos los valores NaN), pero quiero ver el contenido 
    de print(df_eliminados[3]) marcar error, de igual manera si intento verlo 
    como print(df_eliminado[1]) otengo error
"""

import pandas as pd 

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, None, 25, 25],
         "Precio" : [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print('Data Frame original')
print(df)

print('Data Frame con eliminados')
df_eliminados = df.dropna()
print(df_eliminados)



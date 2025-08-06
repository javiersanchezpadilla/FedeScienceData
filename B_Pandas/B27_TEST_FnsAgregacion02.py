""" Dada lista con los siguientes valores de ventas diarias de una tienda en una semana:
    ventas = [120, 150, 90, 200, 210, 130, 160]
    
    REALIZA LAS SIGUIENTES TAREAS:
    * Crea una serie de Pandas con los días de la semana como índice  (asumiendo que el 
      primer valor corresponde al Lunes).
    * Calcula y muestra la suma total de las ventas de la semana. Almacena este valor en 
      una variable llamada: suma_total_ventas
    * Encuentra y muestra el día de mayores ventas. Almacena este valor en una variable 
      llamada: dia_mayores_ventas
    * Calcula y muestra el promedio de ventas de la semana. Almacena este valor en una 
      variable llamada: promedio_ventas
"""

import pandas as pd 

ventas = [120, 150, 90, 200, 210, 130, 160]

serie_ventas = pd.Series(ventas, index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

suma_total_ventas = serie_ventas.sum()
print(suma_total_ventas)

dia_mayores_ventas = serie_ventas.max()
print(dia_mayores_ventas)

promedio_ventas = serie_ventas.mean()
print(promedio_ventas)


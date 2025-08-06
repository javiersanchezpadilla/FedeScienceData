import pandas as pd 

ventas = [120, 150, 90, 200, 210, 130, 160]

serie_ventas = pd.Series(ventas, index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
print(serie_ventas)

suma_total_ventas = serie_ventas.sum()
print(suma_total_ventas)

dia_mayores_ventas = serie_ventas.max()
print(dia_mayores_ventas)

promedio_ventas = serie_ventas.mean()
print(promedio_ventas)

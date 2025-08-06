""" Funciones de agregación:
    sum(), mean(), median(), min(), max(), count(), y std() (desviación estándar)."""


import pandas as pd 

numeros = pd.Series([10, 20, 30, 40, 50])

promedio = numeros.mean()
sumatoria = numeros.sum()
maximo = numeros.max()
minimo = numeros.min()
elementos = numeros.count()
desviacion_estandar = numeros.std()

print(f'El valor promedio de la serie es      : {promedio}')
print(f'La suma de todos los valores  es      : {sumatoria}')
print(f'El valor máxico de la serie es        : {maximo}')
print(f'El valor mínimo de la serie es        : {minimo}')
print(f'El total de elementos de la serie es  : {elementos}')
print(f'La desviación estandar de la serie es : {desviacion_estandar}')



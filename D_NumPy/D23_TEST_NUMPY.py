""" Este proyecto consiste en analizar un conjunto de datos meteorológicos 
    utilizando Python y NumPy. 
    El objetivo es aplicar las técnicas de manipulación de arrays, 
    tratamiento de datos faltantes, y análisis estadístico básico en un 
    conjunto de datos del mundo real.

    Tareas a Realizar:

    1. Crear un DataFrame a partir de los datos del archivo 
       datos_meteorologicos.csv.
    2. Realizar observaciones iniciales de los datos con Pandas.
    3. Convertir las columnas del DataFrame en arrays de NumPy.
    4. Identificar los datos faltantes en los arrays, y reemplazarlos por 
       el promedio de los valores del respectivo array.
    5. Realizar análisis estadísticos básicos. Mínimamente se espera que 
       puedas extraer la siguiente información de tus arrays:
        * La temperatura promedio
        * El total de precipitaciones
        * La máxima humedad registrada
        * La fecha más calurosa
        * La fecha más fría

    6. Exportar los resultados a un nuevo archivo CSV.
"""

import numpy as np 
import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/datos_meteorologicos.csv'


#  1. Crear un DataFrame a partir de los datos del archivo 
#     datos_meteorologicos.csv.
df = pd.read_csv(ruta)
# print(df)


#  2. Realizar observaciones iniciales de los datos con Pandas.
# Aqui lo interesante es que si tenemos un total de 5110 registros
# y otenemos menos de esos valores no nulos entonces tenemos ahi algo
# que hacer
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5110 entries, 0 to 5109           <-- 5110 valores en total
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Fecha          5110 non-null   object    <-- Sin valores nulos
#  1   Temperatura    4855 non-null   float64   <-- 255 valores nulos
#  2   Precipitación  4855 non-null   float64   <-- 255 valores nulos
#  3   Humedad        4855 non-null   float64   <-- 255 valores nulos
# dtypes: float64(3), object(1)
# memory usage: 159.8+ KB
# None

print(df.info())



print(df.head())
print(df.describe())

# print('\nAnalizamos los valores nulos')
# print(df.isnull().sum())
# print('\nForma del data frame')
# filas, columnas = df.shape
# print('Filas:', filas, ', Columnas:', columnas)


#  3. Convertir las columnas del DataFrame en arrays de NumPy.

temperatura = df['Temperatura'].to_numpy()
precipitacion = df['Precipitación'].to_numpy()
humedad = df['Humedad'].to_numpy()

print('Temperatura en arreglo')
print(temperatura)

print('Precipitación en arreglo')
print(precipitacion)

print('Humedad en arregl')
print(humedad)


#  4. Identificar los datos faltantes en los arrays, y reemplazarlos por 
#     el promedio de los valores del respectivo array.

# Identificar los datos faltantes con isnan
temp_nulo = np.isnan(temperatura)
precip_nulo = np.isnan(precipitacion)
humedad_nulo = np.isnan(humedad)

# identificar el promedio de cada array (ignorando los NaN Not a Number)
temp_promedio = np.nanmean(temperatura)
precip_promedio = np.nanmean(precipitacion)
humedad_promedio = np.nanmean(humedad)

# Reemplazar valores nulos por los promedios
temperatura[temp_nulo] = temp_promedio
precipitacion[precip_nulo] = precip_promedio
humedad[humedad_nulo] = humedad_promedio 

# Otra forma de hacer lo mismo usando el métido numpy.where(,,)
temp_corregido = np.where(np.isnan(temperatura), temp_promedio, temperatura)
precip_corregido = np.where(np.isnan(precipitacion), precip_promedio, precipitacion)
humedad_corregido = np.where(np.isnan(humedad), humedad_promedio, humedad)

print(temp_corregido)
print(temperatura)




#  5. Realizar análisis estadísticos básicos. Mínimamente se espera que 
#     puedas extraer la siguiente información de tus arrays:
#      * La temperatura promedio
#      * El total de precipitaciones
#      * La máxima humedad registrada
#      * La fecha más calurosa
#      * La fecha más fría

temperatura_promedio = np.mean(temperatura)
print('Temperatura promedio', temp_promedio)
print('Temperatura promedio desde todos', temperatura_promedio)

# Total de precicipitaciones
total_precipitaciones = np.sum(precipitacion)
print('El total de precipitaciones', total_precipitaciones)

# Maxima humedad registrada
humedad_maxima = np.max(humedad)
print('Máxima humedad registrada', humedad_maxima)

# LA FECHA MAS CALUROSA

# identifica la temperatura mas alta
mas_calor = np.max(temperatura)
print(mas_calor)

# Registro correspondiente a la temperatura mas alta
# cuando usamos np.where con una sola condicion nos va a devolver una tupla 
# de array (array([2749]),) cada array de esa tupla contiene los indices de 
# los elementos que cumplen la condición en cada dimension del array original
registro_mas_caluroso = np.where(temperatura == mas_calor)#[0][0]
print('Registro de la temperatura mas alta')
print(registro_mas_caluroso)

# de esta forma se puede acceder al array fuera de la tupla, del array de todos 
# los indices donde la condicion es verdadera, en este caso solo fue uno, pero 
# podrian haber sido mas
registro_mas_caluroso = np.where(temperatura == mas_calor)[0] #[0]
print(registro_mas_caluroso)

# Ahora accedo a ese primer elemento dentro del arreglo
# realmente se accede al primer índice del primer array
registro_mas_caluroso = np.where(temperatura == mas_calor)[0][0]
print(registro_mas_caluroso)

# Ahora accedemos a la fecha que es lo que nos interesa
fecha_mas_calurosa = df.iloc[registro_mas_caluroso]['Fecha']
print('La fecha mas calurosa es', fecha_mas_calurosa)


# PARA CALCULAR LA FECHA MAS FRIA
fecha_mas_fria = df.iloc[np.where(temperatura == np.min(temperatura))[0][0]]['Fecha']
print('La fecha con la temperatura mas fria es', fecha_mas_fria)


#  6. Exportar los resultados a un nuevo archivo CSV.
# Creamos un data frame con los resultados

resultados = pd.DataFrame({'Metrica' : ['Temperatura promedio', 'Precipitacion Total', 
                                        'Humedad Máxima', 'Día más caluroso', 'Día más frio'],
                           'Valor' : [temperatura_promedio, precip_corregido, humedad_maxima,
                                      fecha_mas_calurosa, fecha_mas_fria]})

# Guardamos los resultados en un archivo CSV
resultados.to_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/resultados_datos_meteorologicos.csv', index=False)

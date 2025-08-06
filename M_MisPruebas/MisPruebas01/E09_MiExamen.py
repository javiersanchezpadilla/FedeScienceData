""" Realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de medallas 
    olímpicas utilizando Pandas. Este proyecto le permitirá aplicar los conceptos aprendidos 
    sobre Series, DataFrames, limpieza de datos, operaciones básicas, filtrado y agregación 
    en Pandas.

    Consigna:

    Contamos con el archivo medallas.csv, que incluye información sobre las medallas de 
    oro, plata, bronce y el total obtenido por cada pais en los Juegos Olimpicos
    Vas a realizar una serie de tareas básicas, que te permitirán responder a las preguntas 
    del siguiente cuestionario:

    1. Cargar los Datos: Importar los datos desde el archivo CSV a un DataFrame de Pandas
    2. Exploración Inicial: Utilizar métodos básicos para explorar el tamaño, las columnas 
       y los tipos de datos del Data Frame.
    3. Limpieza de Datos: Identificar y manejar valores faltantes o incorrectos, especialmente 
       en las columnas de medallas donde los valores faltantes indican cero medallas.
    4. Análisis de Medallas por País: Realiza las operaciones que sean necesarias para 
       identificar cuáles fueron los 3 países con más medallas de oro en total (va a necesitar 
       investigar los métodos de data frames para encontrar cuál le permite ordenar los valores 
       de mayor a menor o viceversa).
    5. Análisis de Medallas Totales por País: Obtener un data frame que contenga sólo los 
       países que ganaron más de 10 medallas en total.

"""
import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/medallas.csv'

df = pd.read_csv(ruta)
# print(df)

# Exploracion básica
print('Tamaño del data frame', df.shape)
print('Nombres de las series ', df.columns)
print(df.head(3))
print(df.tail(3))
print('\nInformación del data frame', df.info())
print('Descripción del data frame', df.describe())
print('Valores nulos NaN', df.isna())
print('Resumen de valores nulos NaN\n', df.isna().sum())

# Cambiamos valores nulos por ceros
df_rellenado = df.fillna(0)
print(df_rellenado.isna().sum())

# Cambiarmos las columnas de Oro, Plata, Bronce por enteros
df_rellenado['Oro'] = df_rellenado['Oro'].astype(int)
df_rellenado['Plata'] = df_rellenado['Plata'].astype(int)
df_rellenado['Bronce'] = df_rellenado['Bronce'].astype(int)

df_ordenado = df_rellenado.sort_values('Oro', ascending=False).head(3)
print(df_ordenado)

# Solo los paises con mas de 10 medallas
criterio_10 = df_rellenado['Total'] > 10
df_solo_10 = df_rellenado[criterio_10]
print('Paises con mas de diez medallas')
print(df_solo_10)

""" Crear un programa en Python que analice un conjunto de datos de ventas 
    de una tienda. El programa debe realizar varias operaciones de 
    Data Science para proporcionar información valiosa sobre las ventas 
    de la tienda.

    Consigna

    Lectura de Datos: Crea un DataFrame que contenga los datos provistos 
    en el archivo Datos_Ventas_Tienda.csv el archivo contiene información 
    como fecha de venta, categoría de producto, cantidad vendida y precio.

    Fusión de Datos: Crea un segundo DataFrame que contenga los datos del 
    archivo Datos_Ventas_Tienda2.csv. y concatenarlos para tener un solo 
    dataFrame con toda la información.

    Tratamiento de Datos: Utiliza Pandas para manipular estos datos. 
    Deberás realizar tareas como limpieza de datos, filtrado y transformaciones 
    básicas.

    Análisis de Ventas: Realiza análisis para responder preguntas como:
    • ¿Cuál es el producto más vendido?
    • ¿Cuál es el mes con más ventas?

    Datos Agrupados: Agrupa los datos por categoría de producto y analiza las 
    ventas por categoría

    Guardar Resultados: Al final, guarda el DataFrame completo (incluyendo 
    la columna de meses) en un archivo .csv en tu máquina.
"""

import pandas as pd 


ruta1 = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Datos_Ventas_Tienda.csv'

ruta2 = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Datos_Ventas_Tienda2.csv'

# CReamos los data frame de cada archivo de ventas
df_ventas1 = pd.read_csv(ruta1)
df_ventas2 = pd.read_csv(ruta2)


# concatenamos los datos de ambos data frame y resetamos 
# el índice
df = pd.concat([df_ventas1, df_ventas2], ignore_index=True)

# Comenzamos a analizar datos para la limpieza de datos
# convertimos la columna de fecha a una fecha real
df['Fecha'] = pd.to_datetime(df['Fecha'])
#print(df)

# Analizamos la información contenida en el data frame DF.INFO()
# Primero tenemos que hacer la limpieza para poder avanzar y contar
# con información homogenea

print(df.info())

# RangeIndex: 1050 entries, 0 to 1049           <-- Tenemos 1050 entradas
# Data columns (total 5 columns):               <-- cinco columnas
#  #   Column           Non-Null Count  Dtype         
# ---  ------           --------------  -----         
#  0   Fecha            1050 non-null   datetime64[ns]  <-- 1050 fechas no nulas
#  1   Producto         1050 non-null   object  <-- Producto 1050 valores de texto
#  2   Cantidad         1050 non-null   int64   <-- Cntidad 1050 valores enteros
#  3   Precio Unitario  1050 non-null   int64   <-- Precio 1050 valores no nulos
#  4   Total Venta      1050 non-null   int64   <-- Total venta 1050 valores no nulos
# dtypes: datetime64[ns](1), int64(3), object(1)<-- resumen de los tipos de datos
# memory usage: 41.1+ KB
# None




# PRoducto mas vendido. Vamos a sumar cuanto vendio cada producto
# vamos a agrupar por producto y vamos a obener la suma de cada uno de ellos
# Aqui solo agrupa los producos totales pero no me dice cual fue el mas vendido
producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum()

# Ahora ordenamos los resultados del mayor al menor para saber el mas vendido
producto_mas_vendido = producto_mas_vendido.sort_values(ascending=False)
print(producto_mas_vendido.head(1))



# ¿Cual es el mes de mas ventas?
# debo extraer el mes de la fecha para organizar y agrupar por med
meses = []
for f in df['Fecha']:
    meses.append(f.month)

# creamos una nueva serie que conenga los meses de la fecha
df['Meses'] = meses

# Agrupamos por mes y en cada mes suamos el Total de Ventas
ventas_por_mes = df.groupby('Meses')['Total Venta'].sum().sort_values(ascending=False)
print(ventas_por_mes.head(1))



ventas_por_categoria = df.groupby('Producto')['Total Venta'].sum()
print(ventas_por_categoria)

# Datos Agrupados: Agrupa los datos por categoría de producto y analiza las 
# ventas por categoría
# Name: Total Venta, dtype: int64
# Producto
# Alimentos      12620          <-- Es el que nos deja menos dinero
# Electrónic    244000          <-- Tiene mas ventas que los demas
# Juguetes       33390
# Libros         20840
# Ropa           56400
# Name: Total Venta, dtype: int64



# Guardar Resultados: Al final, guarda el DataFrame completo (incluyendo 
# la columna de meses) en un archivo .csv en tu máquina.
ruta_final = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Datos_Ventas_Tienda_FINAL.csv'

df.to_csv(ruta_final)
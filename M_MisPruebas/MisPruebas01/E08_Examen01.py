import pandas as pd 

""" Punto 1. Carga de datos."""
ruta = "/home/javier/Documentos/Programas/Python/FedeScienceData/Z_ArchivosExternos/medallas.csv"
df = pd.read_csv(ruta)

"""Punto 2 Exploración inicial.
   Usaremos los metodos y atributos mas comunes para explorar nuestra hoja de calculo."""

# Shape no es un método es un atributo y permite conocer el número de filas y columnas 
# de un dataFrame
print("SHAPE")
print(df.shape)

# Con la función head() podemos ver las primeras cinco líneas del archivo para ver cómo 
# se compone el archivo sin necesidad de tener que visualizar todo el archivo.
print('HEAD')
print(df.head())

# El método tail (cola) nor permite conocer las últimas cinco líneas del archivo
print("TAIL")
print(df.tail())

# columns es un atributo de un Data Frame que devuelve un objeto Index que contiene 
# los nombres de las columnas del DataFrame. Esto nos permitira identificar de manera 
# más sencilla las series.
print('Nombres de las Columnas')
print(df.columns)

# info( ) Permite obtener un resumen de nuestro data Frame de trabajo, es un compendio
# de información importante.
print('Informacion del archivo')
print(df.info())

# describe() Nos da un resumen de los datos del dataFrame.
print('Dercripción del archivo')
print(df.describe())

# isnull() determina dentro del data frame si existen valores nulos y los identifica
# en forma de tabla
print(df.isnull())

# isnull().sum() para sumar el total de valores nulos en cada serie o columna
print(df.isnull().sum())


""" Punto 3. Limpieza de datos"""

# Reemplazar valores no validos, los valores vacion los cambiaremos por ceros
df_relleno = df.fillna(0)
print(df_relleno)
# tambien podemos hacer que rellene con ceros y modifique el data frame original
# esto con el argumento inplace=True
# df.fillna(0, inplace=True)


# Corregir los tipos de datos
df = df_relleno

df['Oro'] = df['Oro'].astype(int)
df['Plata'] = df['Plata'].astype(int)
df['Bronce'] = df['Bronce'].astype(int)

print(df)

""" Punto 4. Analisis de medallas de oro por pais"""
top_3_oro = df.sort_values('Oro', ascending=False).head(3)
print(top_3_oro)


""" Punto 5. Análisis de Medallas Totales por País: Obtener un data frame que contenga 
    sólo los países que ganaron más de 10 medallas en total"""
filtro = df['Total'] > 10
mas_de_10_medallas = df[filtro]
print(mas_de_10_medallas.sort_values('Total', ascending=False))

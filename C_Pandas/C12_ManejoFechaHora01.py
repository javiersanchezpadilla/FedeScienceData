""" Generalmente no es común que nosotros manejemos la creación
    de las fechas o las horas, lo común es que recibamos archivos 
    que contienen series que representan fechas u horas, pero que
    nosotros tenemos que conertir para poder manipularlas, el archivo
    contiene datos de la bolsa de valores
    
    En este ejercicio vamos a convertir una serie de texto a timestamp
    
            df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

    """

import pandas as pd 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Mercado+de+Valores+España.csv'

df = pd.read_csv(ruta)
print(df)

# Imprimimos un elemento de la serie que aparentemente es del tipo de fecha
print(df['Fecha'][0])


# Verificamos el tipo de dato al que pertenece
print(type(df['Fecha'][0]))

# Convertimos los datos de la columna de fecha string a fecha datestamp
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

print(df)
# Imprimimos un elemtos 
print(df['Fecha'][0])
# Verificamos el tipo de dato al que pertenece
print(type(df['Fecha'][0]))


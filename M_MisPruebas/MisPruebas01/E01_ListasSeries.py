import pandas as pd 

ruta='/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Precipitaciones.csv'

df = pd.read_csv(ruta)
print(df.head())

# EXTRAYENDO UNA SERIE DE UN DATA FRAME <<<<<<<<<<<<<<<<<<<
serie = df['region']
print(serie)
print(serie.head())
print(serie.tail())

# PODEMOS CONVERTIR LISTAS DE PYTHON EN SERIES <<<<<<<

lista = [10, 20, 30, 40, 50, 60, 70]
serie_convertida = pd.Series(lista)
print(serie_convertida)


# CAMBIANDO EL ÍNDICE A LA SERIE (indice personalizado)<<<<<<<<<<<<<

datos_en_lista = [1, 2, 3, 4, 5, 6, 7, 8]
indice_para_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']

serie_convertida2 = pd.Series(datos_en_lista, indice_para_lista)
print(serie_convertida2)
print(serie_convertida2['a'])
print(serie_convertida2['b'])
print(serie_convertida2['c'])
            # Explicar lo de la inclusion de los indices personalizados
print(serie_convertida2['b':'f'])

# CONVERTIR UN DICCIONARIO A UNA SERIE key es el índice y valor el valor <<<<<<<<<<<<<<<
capitales = {'Guerrero': 'Chilpancingo', 'Jalisco': 'Guadalajara', 
             'Colima': 'Colima', 'Morelos': 'Cuernavaca'}
serie = pd.Series(capitales)

# OPERACIONES BÁSICAS CON LAS SERIES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
serie_convertida2 = serie_convertida2 + 100
print(serie_convertida2)
serie_convertida2 = serie_convertida2 * 2
print(serie_convertida2)
serie_convertida2 = serie_convertida2 - 50
print(serie_convertida2)
serie_convertida2 = serie_convertida2 ** 2
print(serie_convertida2)




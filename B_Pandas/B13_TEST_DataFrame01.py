""" Crea un DataFrame llamado datos_clima usando Pandas para cargar un archivo CSV llamado "clima.csv"
    que supuestamente contiene datos sobre temperaturas y precipitaciones en diferentes ciudades. 
    Asegúrate de importar Pandas antes de intentar cargar el archivo.

    Considera que tu archivo "clima.csv" se encuentra en la misma ubicación que el archivo de tu código, 
    por lo cual puedes importarlo usando su nombre incluyendo la extensión .csv
"""
import pandas as pd 

datos_clima = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/clima.csv')

print(datos_clima)

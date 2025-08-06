import pandas as pd 
import numpy as np 

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/Ciudades_Visitadas_Latinoamerica_2023.csv'

df = pd.read_csv(ruta)

print(df)
print('\nOpers que haciamos en pandas pero que ahora hacemos con NumPy')
print('\nOperaciones con pandas')
print('El promedio de la población es',df['Población'].mean())
print('El valor mínimoo de la población es',df['Población'].min())
print('El valor máximo de la población es',df['Población'].max())

print('\nOperaciones con NumPys')
print('El promedio de la población es', np.mean(df['Población'])) #   round(df['Población'].mean()))
print('El promedio redondeado es', np.round(df['Población'].mean()))
print('El valor minimo de los visitantes es', np.min(df['Visitantes']))
print('El valor máximo de los visitantes es', np.max(df['Visitantes']))


import pandas as pd 

valores = {'Nombre': ['Juan', 'Karla', 'Dulce'],
           'Edad'   : [20, 25, 40]}

mi_data_frame = pd.DataFrame(valores)

ruta = '/home/\
javier/Documentos/\
Programas/Python/\
FedeScienceData/\
Z_ArchivosExternos/\
Precipitaciones.csv'


print('Esta es una cadena \
cortada en \
varias partes')

print("""Esta es 
una forma 
de colocar 
cadenas 
que son de 
tamaño grande""")


# otro_df = pd.read_csv('/home/javier/Documentos/Programas/Python/FedeScienceData/\
  #                    Z_ArchivosExternos/Precipitaciones.csv')


print(ruta)
#print(otro_df)

# print(valores)
# print(valores['Nombre'])
# print(valores['Nombre'][1])

# print(valores['Edad'])
# print(valores['Edad'][2])

# print(type(valores))
# print(type(valores['Nombre']))
# print(type(valores['Edad']))

# print(type(valores['Nombre'][0]))
# print(type(valores['Edad'][1]))

# print('Valores de mi data frame\n', mi_data_frame)
# print('El tipo de dato del data frame es :', type(mi_data_frame))
# print('El tipo de dato de nombre es ', type(mi_data_frame['Nombre']))
# print('El tipo de dato de nombre, primer valor es ', type(mi_data_frame['Nombre'][0]))
# print('El tipo de dato de Edad es ', type(mi_data_frame['Edad']))
# print('El tipo de dato de Edad, ultimo valor es ', type(mi_data_frame['Edad'][2]))
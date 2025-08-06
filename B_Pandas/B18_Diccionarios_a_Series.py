""" En este ejercicio cambiaremos el tipo de dato diccionario
    a una serie, lo interesante es la conversion que hace
    donde las llaves del diccionario se transforma en el índice"""


import pandas as pd 

capitales = {'Guerrero': 'Chilpancingo', 'Jalisco': 'Guadalajara', 
             'Colima': 'Colima', 'Morelos': 'Cuernavaca'}
serie = pd.Series(capitales)
print(serie)

print('\nREFERENCIANDO LOS ELEMENTOS DE LA NUEVA SERIE A TRAVES DE SU NUEVO ÍNDICE')
print('Elemento 1:', serie['Guerrero'])
print('Elemento 2:', serie['Jalisco'])
print('Elemento 3:', serie['Colima'])
print('Elemento 4:', serie['Morelos'])


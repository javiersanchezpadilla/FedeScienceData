import pandas as pd 

capitales = { 'Guerrero': 'Chilpancingo', 'Jalisco': 'Guadalajara',
              'Colima': 'Colima', 'Veracruz': 'Jalapa', 
              'Baja California' : 'Mexicali'}

mi_serie = pd.Series(capitales)
print(mi_serie)

print(mi_serie['Guerrero'])
print(mi_serie['Guerrero':'Colima'])

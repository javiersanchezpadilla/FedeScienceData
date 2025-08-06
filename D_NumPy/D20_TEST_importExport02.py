""" Dado el archivo 'datos.csv'
    Utiliza la función de NumPy correcta para importar los 
    datos que contienen solo números. Asegúrate de que el 
    delimitador utilizado en el archivo sea una coma (,)
    Asegurate de que se ignoren los encabezados de columna.
    Guarda los datos importados en una variable llamada datos.
    Asegurate de no modificar la ruta que ya viene cargada por 
    defecto en el ejercicio:
    # Cargamos los datos del archivo 'datos.csv', 
    ruta = 'datos.csv'

"""
import numpy as np 

ruta = 'datos.csv'
datos = np.genfromtxt(ruta, delimiter=',', skip_header=1)

print(datos)

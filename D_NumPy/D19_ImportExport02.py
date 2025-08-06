""" En este programa EXPORTAREMOS a un archivo CSV."""

import numpy as np 

array_ejemplo = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

print('\nArray a exportar:\n', array_ejemplo)

ruta = '/home/javier/Documentos/Programas/Python/FedeScienceData/\
Z_ArchivosExternos/miarchivonumpy.csv'

# FORMA 1 Exportando los valores con notacion cientifica
# en este intento los valores se escribiran en el archivo
# usando notación cientifica

# np.savetxt(ruta, array_ejemplo, delimiter=',')
# 1.000000000000000000e+00,2.000000000000000000e+00,3.000000000000000000e+00
# 4.000000000000000000e+00,5.000000000000000000e+00,6.000000000000000000e+00
# 7.000000000000000000e+00,8.000000000000000000e+00,9.000000000000000000e+00


# INTENTO 2 Este es el mas adecuado para respetar los valore
# originales.
# antes de ejecutar debemos borrar en caso de existir el arhivo creado 
# anteriormente o de lo contrario marcará un error
np.savetxt(ruta, array_ejemplo, delimiter=',', fmt='%d')

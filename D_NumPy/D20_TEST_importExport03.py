""" Después de realizar algunas operaciones con arrays de NumPy 
    en tu código, tienes un array llamado resultados

        resultados = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    El cual deseas exportar a un archivo CSV llamado 
    'resultados_finales.csv'.

    Usa la función adecuada de NumPy para lograr esta tarea, 
    asegurándote de que el delimitador sea una coma (,)
"""

import numpy as np

resultados = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('resultados_finales.csv', resultados, delimiter=',')

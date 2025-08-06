""" Uso del manejo de AXIS.
    Concatenar por axis=0 (Filas - vertical):

    Piensa en 'apilar' las matrices una encima de la otra.
    Las columnas deben coincidir (tener el mismo número de elementos).
"""

import numpy as np 

# Ventas Semana 1 (Filas: Días, Columnas: Productos A, B)
ventas_sem1 = np.array([[10, 20],  # Lunes
                        [30, 40]]) # Martes
print("Ventas Semana 1:\n", ventas_sem1)

# Ventas Semana 2 (Filas: Días, Columnas: Productos A, B)
ventas_sem2 = np.array([[50, 60],  # Miércoles
                        [70, 80]]) # Jueves
print("\nVentas Semana 2:\n", ventas_sem2)


# Concatenar por filas (axis=0): Unimos los días de venta
ventas_total_dias = np.concatenate((ventas_sem1, ventas_sem2), axis=0)
print("\nConcatenado por FILAS (axis=0 - apilando días):\n", ventas_total_dias)
# Resultado esperado:
# [[10 20]  <- Lunes (Semana 1)
#  [30 40]  <- Martes (Semana 1)
#  [50 60]  <- Miércoles (Semana 2)
#  [70 80]] <- Jueves (Semana 2)

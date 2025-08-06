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


# Ahora, imagina que tienes ventas de Productos C y D para la misma Semana 1
# Y quieres añadirlas como nuevas columnas a las ventas existentes
nuevos_productos_sem1 = np.array([[ 5, 15],  # Lunes (Productos C, D)
                                  [25, 35]]) # Martes (Productos C, D)
print("\nNuevos Productos Semana 1:\n", nuevos_productos_sem1)


# Concatenar por columnas (axis=1 - pegando productos):
ventas_total_productos = np.concatenate((ventas_sem1, nuevos_productos_sem1), axis=1)
print("\nConcatenado por COLUMNAS (axis=1 - añadiendo productos):\n", ventas_total_productos)
# Resultado esperado:
# [[10 20  5 15] <- Lunes (Prod A, B, C, D)
#  [30 40 25 35]] <- Martes (Prod A, B, C, D)

""" Uso de las funciones universales. UFUNCS
    NumPy.ADD()        Para sumar
    NumPy.SUBSTRACT()  Restar
    NumPy.MULTIPLY()   Multiplicar
    NumPy.DIVIDE()     Dividir

"""
import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

suma = np.add(a, b)
resta = np.subtract(a, b)
multip = np.multiply(a, b)
dividir = np.divide(a, b)

print('OPERACIONES UNIVERSARLES\n')
print('Arrays originales: a-->', a)
print('Arrays originales: b-->', b)

print('\nSuma de arrays:        ', suma)
print('Resta de arrays:       ', resta)
print('Producto de arrays:    ', multip)
print('Division de arrays:    ', dividir)

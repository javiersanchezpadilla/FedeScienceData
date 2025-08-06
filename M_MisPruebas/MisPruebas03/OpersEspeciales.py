""" Este modulo permite realizar operaciones especiales
    incluidas en la libreria math
    Las operaciones a realizar son:
    Potencia a la 'n', raiz cuadrada y factorial"""

import math as m 

def potencia(base, exponente):
    """ Permite elevar un numero al exponente
    
        ARgumentos:
            base  valor base del calculo, es un valor entero
            exponente  exponente, es un valor enterio
            
        Retorna:
            UN valor entero"""
    return m.pow(base, exponente)

def raiz(valor):
    """.....Toda la documentación de la funcion para
        calcular la raiz cuadrada"""
    return m.sqrt(valor)


def factorial(valor):
    """.....Toda la documentación de la funcion para
        calcular la raiz cuadrada"""
    return m.factorial(valor)


if __name__ == '__main__':
    print('3 elevado a la 3=', potencia(3,3))
    print('Raiz cuadrada de 81', raiz(81))
    print('El factorial de 5 =', factorial(5))
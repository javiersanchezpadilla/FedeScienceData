""" Programa que permite realizar las operaciones básicas
    de una calculadora (suma, resta, multiplicación y división)."""


def sumar(a, b):
    """ Funcion que permite la suma de dos valores
    
        Argumentos:
        a   valor entero o flotante
        b   valor entero o flotante
        
        Retorna:
        Un valor entero"""
    return a + b


def restar(a, b):
    """ Funcion que permite la resta de dos valores
    
        Argumentos:
        a   valor entero o flotante
        b   valor entero o flotante
    
        Retorna:
        Un valor entero o fracción """
    return a - b


def multiplicar(a, b):
    """ Funcion que permite la multiplicación de dos valores
    
        Argumentos:
        a   valor entero o flotante
        b   valor entero o flotante
        
        Retorna:
        El calculo de la diferencia de los valores"""
    return a * b


def dividir(a, b):
    """ Funcion que permite dividir dos valores
    
        Argumentos:
        a valor entero o flotante
        b valor entero o flotante
        
        Retorna:
        El resultado de la division en un valor flotante o enter"""
    return a / b


if __name__ == '__main__':
    print('La suma de 10+20=', sumar(10, 20))
    print('LA diferencia de 10-2=', restar(10, 2))
    print('El producto de 10*3=', multiplicar(10, 3))
    print('LA división de 10/3=', dividir(10, 3))
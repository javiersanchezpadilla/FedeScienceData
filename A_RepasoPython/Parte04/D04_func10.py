""" Argumentos variables en funciones """

def sumaDos(a, b):
    return a + b

def sumaTres(a, b, c):
    return a + b + c

def sumaCuatro(a, b, c, d):
    return a + b + c + d

def sumaMuchos(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(sumaDos(10,10))
print(sumaTres(10,10,10))
print(sumaCuatro(10,10,10,10))
print(sumaMuchos(10,10,10,10,1,2,3,4,5,6,7,8,9,9,0,5,4,4,5,6,77))

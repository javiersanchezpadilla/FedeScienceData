""" argumentos fijos y argumentos variables en funciones   """

def suma_valores(a, b, *args):
    suma = a + b
    for n in args:
        suma += n
    return suma

print(suma_valores(10, 20))
print(suma_valores(10, 20, 30))
print(suma_valores(10, 20, 30, 40, 50))
print(suma_valores(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


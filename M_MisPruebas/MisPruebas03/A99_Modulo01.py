""" Definicion de una clase"""

class calculos:
    """ Clase calculos Permite realiar operaciones basicas
        argumentos:
        debe recibir dos valores enteros
    
        metodos:
        suma    PErmite sumar dos valores
        resta   Permite restar dos valores"""

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2
    
    def resta(self):
        return self.valor1 - self.valor2
    

if __name__ == '__main__':
    a = calculos(10,5)
    print('La suma es :', a.suma())
    print('La resta es:', a.resta())


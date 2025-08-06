# Definicion de una variale

variable = 'Soy una variable'


# Definicion de las funciones

def sumar_por_funcion(valor1, valor2):
    return valor1 + valor2


def restar_por_funcion(valor1, valor2):
    return valor1 - valor2


def multiplicar_por_funcion(valor1, valor2):
    return valor1 * valor2

# Definicion de las clases.

class OpersBasicas:

    def __init__(self, valor_a, valor_b):
        self.valor_a = valor_a
        self.valor_b = valor_b

    def sumar_por_clase(self):
        return self.valor_a + self.valor_b
    
    def restar_por_clase(self):
        return self.valor_a - self.valor_b

    def multiplicar_por_clase(self):
        return self.valor_a * self.valor_b

if __name__ == '__main__':
    print('\nTomando el valor de las variables')
    print(variable)

    print('\nUsando las funciones')
    print(sumar_por_funcion(10,5))
    print(restar_por_funcion(40, 30))
    print(multiplicar_por_funcion(2, 8))

    print('\nUsando la clase y sus métodos')
    calculo = OpersBasicas(10, 5)
    print(calculo.sumar_por_clase())
    print(calculo.restar_por_clase())
    print(calculo.multiplicar_por_clase())

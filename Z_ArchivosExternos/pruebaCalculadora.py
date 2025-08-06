class OpersBasicas:

    def __init__(self, valor_a, valor_b):
        self.valor_a = valor_a
        self.valor_b = valor_b

    def sumar(self):
        return self.valor_a + self.valor_b
    
    def restar(self):
        return self.valor_a - self.valor_b
    
    def multiplicar(self):
        return self.valor_a * self.valor_b

    def dividir(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    a = OpersBasicas(10, 2)
    print(a.sumar())
    print(a.restar())
    print(a.multiplicar())
    print(a.dividir())

import OpersBasicas as ob
import OpersEspeciales as oe


def que_valores(valor1, valor2):
    valor1 = int(input('Primer valor'))
    valor2 = int(input('Segunfo valor'))
    return valor1, valor2


opcion = None
numero1 = 0
numero2 = 0

while opcion != 0:
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 dividir')
    print('5 Potencia')
    print('6 Raiz cuadrada')
    print('7 factorial')
    print('0 salir')
    opcion = int(input('Opcion:'))

    if opcion != 0:
        numero1, numero2 = que_valores(numero1, numero2)
    else:
        print("Hasta la vista...")
  
    if opcion == 1:
        print(f'La suma de {numero1} + {numero2} =', ob.sumar(numero1, numero2))
    elif opcion == 2:
        print(f'La diferencia de {numero1} - {numero2} =', ob.restar(numero1, numero2))
    elif opcion == 3:
        print(f'El producto de {numero1} * {numero2} =', ob.multiplicar(numero1, numero2))
    elif opcion == 4:
        print(f'Dividir {numero1} / {numero2} =', ob.dividir(numero1, numero2))
    elif opcion == 5:
        print(f'{numero1} elevado a la {numero2} potencia =', oe.potencia(numero1, numero2))
    elif opcion == 6:
        print(f'Laraiz cuadrada de {numero1}  =', oe.raiz(numero1))
    elif opcion == 7:
        print(f'El factoria de {numero1} =', oe.factorial(numero1))



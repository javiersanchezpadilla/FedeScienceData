num1 = 1  # 1 1 1 1 3 2
num2 = 2  # 1 1 3 2 2 3
num3 = 3  # 2 1 2 3 1 1

menor = None
medio = None
mayor = None

if num1 == num2 and num1 == num3:
  menor = num1
  medio = num2
  mayor = num3
elif num1 <= num2 and num1 <= num3:
  menor = num1
  if num2 <= num3:
    medio = num2
    mayor = num3
  else:
    medio = num3
    mayor = num2
elif num2 <= num1 and num2 <= num3:
  menor = num2
  if num1 <= num3:
    medio = num1
    mayor = num3
  else:
    medio = num3
    mayor = num1
else:
  menor = num3
  if num1 <= num2:
    medio = num1
    mayor = num2
  else:
    medio = num2
    mayor = num1

# Imprimimos los resultados
print("El orden de los números es:")
print("Menor:", menor)
print("Medio:", medio)
print("Mayor:", mayor)

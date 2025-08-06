# Simulador de maquina de cambio de divisas

nombre = "Javier"
fecha = "20/01/2025"
saludo = "Bunos dias"

bienvenida = saludo + " " + nombre + " Hoy es " \
             + fecha + ". Bienvenido al Servicio de cambio de divisas"

print(bienvenida)


dolares = 272.0
pesos_a_recibir = dolares * 21

billetes_200 = pesos_a_recibir // 200
billetes_100 = (pesos_a_recibir - (billetes_200 * 200)) // 100
billetes_50 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)) // 50 
billetes_20 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100) \
               - (billetes_50 * 50)) // 20
monedas_10 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100) \
              - (billetes_50 * 50) - (billetes_20 * 20)) // 10
monedas_5 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)  \
             - (billetes_50 * 50) - (billetes_20 * 20) - (monedas_10 * 10)) // 5
monedas_1 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)  \
             - (billetes_50 * 50) - (billetes_20 * 20) - (monedas_10 * 10) - (monedas_5 * 5)) // 1


print(f'Cantidad en dolares {dolares}')
print(f'Total en pesos      {pesos_a_recibir}')

print(f'Billetes de 200 {billetes_200}')
print(f'Billetes de 100 {billetes_100}')
print(f'Billetes de 50  {billetes_50}')
print(f'Billetes de 20 {billetes_20}')
print(f'Monedasd de 10 {monedas_10}')
print(f'Monedasd de 5 {monedas_5}')
print(f'Monedasd de 1 {monedas_1}')

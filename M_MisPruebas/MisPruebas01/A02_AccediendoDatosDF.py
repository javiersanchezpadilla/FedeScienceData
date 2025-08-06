import pandas as pd 

valor = {"Sucursal"  : ['Centro', 'Sur', 'Norte', 'Este', 'Oeste'],
         "Empleados" : [5, 4, 5, 6, 4],
         "Ventas"    : [27658, 36548, 12998, 29448, 19853]}

print(valor)

df = pd.DataFrame(valor)
# imprimiendo el data frame
print(df)

# Accediendo a la serie Sucursal
print(df['Sucursal'])

# Accediento a la serie empleados
print(df['Empleados'])

# Accediendo a la serie ventas
print (df['Ventas'])


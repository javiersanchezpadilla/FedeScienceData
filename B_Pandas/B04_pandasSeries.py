import pandas as pd    

datos = {"nombre":["pedro", "Juan", "lorena"], "edad":[25, 39, 20]}

df = pd.DataFrame(datos)

# accediendo a la serie nombre
# Podemos hacerlo mediante el uso de corchete
print(df["nombre"])

# podemos hacerlo mediante el uso del punto y el nombre de la serie
print(df.nombre)
print(type(df.nombre))

import pandas as pd 
import numpy as np

# Desplegar todos los metodos y atributos de pandas

# print(dir(pd))

# Desplegar información sobre un metodo en particular
# print(dir(pd.read_csv))

# Podemos pedir ayuda sobre algo, la ayuda es información
# help(pd)

# Podemos pedir ayuda especifica sobre un metodo
# help(pd.read_csv)

# Para buscar dentro del directoriio de metodos y atributos algo relacionado
# por ejemplo buscar aquellos metodos que contengan la palabra 'to'

# n = [name for name in dir(pd) if 'to' in name]
# print(n)

# por ejemplo para buscar los metodos que contengan la palabra 'csv'
# n = [nombre for nombre in dir(pd) if 'csv' in nombre]
# print(n)

# help(pd.Timedelta)
# help(np)
print(dir(np))

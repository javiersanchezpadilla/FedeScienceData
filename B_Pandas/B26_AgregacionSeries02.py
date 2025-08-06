import pandas as pd

# Crear una serie de ejemplo
data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Aplicar varias funciones de agregación a la columna 'col1'
resultado = df['col1'].agg(['sum', 'mean', 'min', 'max', 'count'])
print(resultado)

# Aplicar una función definida por el usuario
def my_func(x):
    return x.sum() / len(x)

resultado_personalizado = df['col1'].agg(my_func)
print(resultado_personalizado)



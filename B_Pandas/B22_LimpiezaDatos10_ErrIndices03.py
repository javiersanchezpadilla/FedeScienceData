import pandas as pd

data = { "id_producto": [1001, 1002, 1003, 1003],
         "Cantidad_vendida" : [30, None, 25, 25],
         "Precio" : [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print('--- Data Frame original ---')
print(df)

print('\n--- Data Frame con eliminados (índices originales) ---')
df_eliminados = df.dropna()
print(df_eliminados)

# --- Solución: Reiniciar los índices ---
# Usamos .reset_index(drop=True) para crear un nuevo índice de 0 a N-1
df_limpio_con_nuevo_indice = df_eliminados.reset_index(drop=True)

print('\n--- Data Frame con eliminados y CON ÍNDICES REINICIADOS ---')
print(df_limpio_con_nuevo_indice)

# Ahora sí puedes acceder por las nuevas posiciones 0, 1
print('\n--- Accediendo a la fila con índice 0 (nueva posición) ---')
# Usa .loc[] para acceder por la etiqueta del nuevo índice (que es 0)
print(df_limpio_con_nuevo_indice.loc[0])

print('\n--- Accediendo a la fila con índice 1 (nueva posición) ---')
# Usa .loc[] para acceder por la etiqueta del nuevo índice (que es 1)
print(df_limpio_con_nuevo_indice.loc[1])

# O si quieres acceder por posición numérica (aunque aquí coinciden):
print('\n--- Accediendo a la fila en la posición 0 (iloc) ---')
print(df_limpio_con_nuevo_indice.iloc[0])

print('\n--- Accediendo a la fila en la posición 1 (iloc) ---')
print(df_limpio_con_nuevo_indice.iloc[1])

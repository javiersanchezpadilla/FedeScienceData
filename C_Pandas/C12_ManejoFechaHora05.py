import pandas as pd

# Creamos un DataFrame de ejemplo
datos = {
    'Fecha_Str': ['2025/01/31', '2025/02/15', '2025/03/10']
}
df = pd.DataFrame(datos)

print("--- Paso 1: DataFrame Original (tipo string) ---")
print(df)
print(df.dtypes) # Vemos que es 'object' (string)


# --- Paso 2: Convertir la columna a tipo fecha (datetime) ---
# Usamos format para decirle a Pandas cómo leer la cadena original
# Agregamos una nueva serie a nuestro data frame
df['Fecha_Datetime'] = pd.to_datetime(df['Fecha_Str'], format='%Y/%m/%d')

print("\n--- Paso 2: DataFrame con columna convertida a datetime ---")
print(df)
print(df.dtypes) # Ahora 'Fecha_Datetime' es 'datetime64[ns]'

# Puedes ver que el formato por defecto al imprimir es 'AAAA-MM-DD'


# --- Paso 3: Cambiar el formato de PRESENTACIÓN (¡y convertirlo a string!) ---
# Creamos una nueva columna que es la representación de la fecha en formato 'DD/MM/AAAA'

df['Fecha_Formato_Bonito_Str'] = df['Fecha_Datetime'].dt.strftime('%d/%m/%Y')

print("\n--- Paso 3: DataFrame con la fecha en formato 'bonito' (¡pero es string!) ---")
print(df)
print(df.dtypes) # Ahora 'Fecha_Formato_Bonito_Str' es 'object' (string)

# Puedes ver que 'Fecha_Datetime' sigue siendo 'datetime64[ns]'
# Si solo quieres el DataFrame con el formato bonito para mostrarlo o guardar un CSV:
df_para_mostrar = df[['Fecha_Formato_Bonito_Str']].copy()
df_para_mostrar.rename(columns={'Fecha_Formato_Bonito_Str': 'Fecha'}, inplace=True)
print("\n--- DataFrame solo con la columna formateada (para reportes, etc.) ---")
print(df_para_mostrar)
print(df_para_mostrar.dtypes)


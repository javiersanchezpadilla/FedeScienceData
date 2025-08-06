""" En este programa voy a crear un data frame y se va a escribir
    en un archivo de excel (puede ser csv o lo que se requiera)
    
    dataFrame.to_excel(ruta_con_nombre_del_archivo_y_extension)

    En este ejemplo se escribira el archivo y como primer columna
    mostrara el índice
    """

import pandas as pd 

numeros = { 'romanos' : ['I', 'II', 'III', 'IV', 'V'],
            'arabigos': [1, 2, 3, 4, 5],
            'binarios' : ['0001', '0010', '0011', '0100', '0101'],
            'texto' : ['uno', 'dos', 'tres', 'cuatro', 'cinco']}

df = pd.DataFrame(numeros)
print(df)

# Agregamos una serie de fechas
df['fechas'] = pd.Series(pd.date_range('20250101', periods=5))
print(df)

# Vamos a llevarlo a excel
ruta = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/MiArchivoExcelCreado.xlsx'
df.to_excel(ruta)


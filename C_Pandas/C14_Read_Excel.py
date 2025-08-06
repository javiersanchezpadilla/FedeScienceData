""" Ahora vamos a trabajar otro tipo de archivos en Pandas

    En este ejemplo marco un error, pidiendo instalar
    $ pip3 install openpyxl     <-- Para poder leer xlsx
    $ pip3 install lxml         <-- PAra leer los xml
"""

import pandas as pd 

ruta_excel = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Compras_desde_ads.xlsx'

ruta_xml = '/home/javier/Documentos/Programas/Python/\
FedeScienceData/Z_ArchivosExternos/Valores de acciones.xml'

df1 = pd.read_excel(ruta_excel)
print(df1)

# tengo problemas para poder leer archivos xml
# df2 = pd.read_xml(ruta_xml)
# print(df2)


""" Definicion de estilos para los gráficos

        matplotlib.pyplot.style.use('estilo')

    MUY MUY IMPORTANTE!!!!
    ----------------------
    En Matplotlib, cuando ejecutas fig, axs = plt.subplots(), el programa "dibuja" 
    la estructura base del gráfico (el fondo, las rejillas y los ejes) usando 
    el estilo que esté activo en ese preciso momento. Si el estilo se cambia después, 
    los ejes que ya fueron creados no se enteran del cambio, por lo que se debe 
    colocar antes de esa linea.!!!

    Para concer todos los estilos disponibles

        print(plt.style.available)

    'Solarize_Light2'       '_classic_test_patch'       '_mpl-gallery', 
    '_mpl-gallery-nogrid'   'bmh', 'classic'            'dark_background'
    'fast'                  'fivethirtyeight'           'ggplot'
    'grayscale'             'petroff10'                 'seaborn-v0_8'
    'seaborn-v0_8-bright'   'seaborn-v0_8-colorblind'   'seaborn-v0_8-dark'
    'seaborn-v0_8-dark-palette'                         'seaborn-v0_8-darkgrid'
    'seaborn-v0_8-deep'     'seaborn-v0_8-muted'        'seaborn-v0_8-notebook'
    'seaborn-v0_8-paper'    'seaborn-v0_8-pastel'       'seaborn-v0_8-poster'
    'seaborn-v0_8-talk'     'seaborn-v0_8-ticks'        'seaborn-v0_8-white'
    'seaborn-v0_8-whitegrid'                            'tableau-colorblind10'

    Vamos a asignar un estilo visual a nuestros gráficos

    Estilos recomendados:

    'bmh'               Muy profesional para reportes.
    'dark_background'   Genial si usas modo oscuro en tu editor.
    'fivethirtyeight'   Estilo tipo revista de datos/noticias.
"""

import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame({'etiquetas' : ['Manzanas', 'Platanos', 'Naranjas', 'Uvas'],
                   'cantidad' : [30, 35, 26, 33]})

# Lo primero es definir el estilo para que sea la base de la creación
# de nuestros gráficos con base a este estilo
plt.style.use('bmh')

fig, axs = plt.subplots(nrows=1, ncols=2)
ax1 = axs[0]
ax2 = axs[1]

ax1.plot(df['etiquetas'], df['cantidad'])
ax2.pie(df['cantidad'])

# PAra visualizar los estilos disponibles
# print(plt.style.available)
plt.show()

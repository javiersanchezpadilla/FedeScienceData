import pandas as pd

valores = { "Nombre" : ['Juan', 'Pedro', 'Francisco'],
            "Edad" : [25, 39, 29]}

print(valores)          # {'Nombre': ['Juan', 'Pedro', 'Francisco'], 
                        # 'Edad': [25, 39, 29]}
print(type(valores))    # <class 'dict'>

df = pd.DataFrame(valores)
print(df)               #       Nombre  Edad
                        # 0       Juan    25
                        # 1      Pedro    39
                        # 2  Francisco    29

print(type(df))         # <class 'pandas.core.frame.DataFrame'>

print(df['Nombre'][1])  # Pedro
print(type(df['Nombre'][1]))    # <class 'str'>

print(df['Edad'][2])    # 29
print(type(df['Edad'][2]))      # <class 'numpy.int64'>

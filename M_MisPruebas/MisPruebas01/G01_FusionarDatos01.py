import pandas as pd 

df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Ana', 'Luis', 'Carlos']})

df2 = pd.DataFrame({'ID':[1, 2, 4],
                    'Edad': [25, 30, 22]})

print(df1)
print(df2)
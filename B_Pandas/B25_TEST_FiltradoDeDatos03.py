""" Crea una serie de Pandas llamada frutas y que contenga los siguientes elementos: 
    ["manzana", "banana", "cereza", "durazno", "frambuesa"].
    Escribe un código que filtre y muestre solo aquellos elementos que contengan la 
    letra "e" en su nombre. Almacena los elementos filtrados en una variable llamada 
    frutas_con_e
    Utiliza una condición que aplique un método de strings para lograr este filtrado.
"""
import pandas as pd 

frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])
frutas_con_e = frutas.str.contains("e")
print(frutas[frutas_con_e])

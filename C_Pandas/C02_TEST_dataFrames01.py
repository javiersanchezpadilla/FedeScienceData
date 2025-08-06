""" Crea un DataFrame llamado libros_df con la siguiente información 
    sobre libros:
    Los títulos son: "El Quijote", "Cien años de soledad", "La odisea"
    Los autores son "Miguel de Cervantes", "Gabriel García Márquez", "Homero"
    Los años de publicación son 1605, 1967, y -800, respectivamente.
    Asegúrate de utilizar las columnas Titulo, Autor y Año.
"""
import pandas as pd 

libros = { 'Titulo' : [ "El Quijote", "Cien años de soledad", "La odisea"],
           'Autor' : ["Miguel de Cervantes", "Gabriel García Márquez", "Homero"],
           'Año' : [1605, 1967, -800] }
libros_df = pd.DataFrame(libros)
print(libros_df)

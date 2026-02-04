palabra = 'acapulco'

print(palabra.upper())
print(palabra.lower())
print(palabra)
#print(dir(palabra))
print(palabra.capitalize())
# capitalize es un metodo de la clase str, por loque podemos usarlo como
#  str.capitalize(palabra), a diferencia de palabra.capitalize()
#  que es un metodo del objeto palabra, que es una instancia de la clase str
print(str.capitalize(palabra))
print(str.upper(palabra))
print(str.lower(palabra))
print(palabra.count('a'))
print(palabra.count('c')) 
print(str.count(palabra, 'c'))

# desempaquetando los elementos de una cadena
a, b, c, d, e, f, g, h = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# desempaquetando solo el tercer elemento de la palabra acapulco
_, _, a, *_ = palabra
print(a)
print(_)

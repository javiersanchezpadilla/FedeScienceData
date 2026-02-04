# Lista inicial
frutas = ['manzana', 'banana', 'cereza']

# 1. append(elemento): Añade al final
frutas.append('naranja') 
# Resultado: ['manzana', 'banana', 'cereza', 'naranja'] [3, 5]

# 2. insert(índice, elemento): Inserta en posición específica
frutas.insert(1, 'uva') 
# Resultado: ['manzana', 'uva', 'banana', 'cereza', 'naranja'] [1, 3, 4]

# 3. extend(iterable): Añade múltiples elementos al final
frutas.extend(['pera', 'kiwi']) 
# Resultado: ['manzana', 'uva', 'banana', 'cereza', 'naranja', 'pera', 'kiwi'] [3, 4]

# 4. remove(elemento): Elimina la primera ocurrencia del valor
frutas.remove('banana') 
# Resultado: ['manzana', 'uva', 'cereza', 'naranja', 'pera', 'kiwi'] [1, 2, 4]

# 5. pop(índice): Elimina y devuelve el elemento en el índice (o el último si no se especifica)
ultimo = frutas.pop() 

# Resultado: ['manzana', 'uva', 'cereza', 'naranja', 'pera'] (kiwi eliminado) [1, 2, 4]

# 6. sort(): Ordena la lista in-place (alfabéticamente o numéricamente)
frutas.sort() 
# Resultado: ['cereza', 'manzana', 'naranja', 'pera', 'uva'] [3, 6]

# 7. reverse(): Invierte el orden de la lista
frutas.reverse() 
# Resultado: ['uva', 'pera', 'naranja', 'manzana', 'cereza'] [3, 6]

# 8. index(elemento): Devuelve el índice de la primera aparición
indice = frutas.index('manzana') 
# Resultado: 3 [1, 3]

# 9. clear(): Borra todos los elementos
frutas.clear() 
# Resultado: [] [2]

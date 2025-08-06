""" Problema al personalizar los indices, por ejemplo en este caso yo quiero que 
    el índice inice con cero y no con el valor de uno, pero al momento de referencias
    valores pandas tiene problema de ambigueedad entre el valor del índice real y el 
    de la etiqueta, por eso cuando intento imprimir lo valores serie.[5:8] no lo hace
    respecto a la nueva referencia del índice, lo hace con la referencia del valor real
    para corregir esto podemos usar .loc para referenciar al valor de la etiqueta o
    podemos ser explicitos usando iloc para usar los valores de los indices reales que
    inician desde cero"""
import pandas as pd 

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
indice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

serie = pd.Series(lista, indice)
print(serie)

# Contien ambiguedad por lo que no toma el índie personalizado 
# toma el índice real
print('Solución ambigua python no sabe cual tomar')
print(serie[5:8])   

# corrección para que tome el índice por etiqueta .loc
# solo recordar que al usar loc el último valor es inclusivo
print('Tomando el índice por etiqueta')
print(serie.loc[5:8])   

# Solución explicita para indicar que debe tomar el índice original
# Aqui el último valor no es inclusivo
print('\nTomando el índice real (que inicia desde 0)')
print(serie.iloc[5:8])

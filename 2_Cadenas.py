#AUTOR: Alejandro Meza
#FECHA: 15-01-2019
#Repaso de conceptos
#COMENTARIO SIMPLE

'''
    ESTO ES UN COMENTARIO MULTILINEA
'''

cadena = 'Argitxu Azkarrena' #tipado automatico
#se pueden combinar comillas
#estoy 'estudiando'
cadena_doble = "Estoy 'estudiando'"


#operacion
num1=10
num2 = 6.7
sum = num1+num2*10/6 #se respetan reglas de matematicas
#parentesis influyen
print(sum)
print("El resultado es: ",sum) #, concatena


#tipado dinamico
valor = 10
print("El primer valor es: ",valor)

valor = "Alejandro" #tipado dinamico
print("El nuevo valor es: ",valor)




#poner sin comillas implica el uso directo de una variable
print(cadena)
print(cadena_doble)
#con type averiguamos tipo de la variable
print(type(cadena))
print(type(cadena_doble))

###Tipos de datos booleanos
valor = True
print(valor)
'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 19-04-2020
    PROPÓSITO: MOSTRAR EL USO DE LISTAS
'''

lista_vacia = []
print(lista_vacia)

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print(dias)

#para mostrar un elemento en concreto
print(dias[0])

#con -1, empiezo por el ultimo elemento
print(dias[-1])
#Exception : index out of range

#se puede trabajar con sublistas de una manera bastante directa
print(dias[0:3]) #llega a pos n-1

print(dias[1:]) #desde la 1 hasta el final

#Python admite listas con distintos tipos  de datos

#uso de funcion len devuelve numero de elementos de la lista
print(len(dias))
dias.append("sabado")
print(dias)

lista = [1,2,4,5]
#agregar el 3 en la posicion correcta
lista.insert(2,3) #index, object
print(lista)

#podemos agregar tambien mas de un elemento --> concatenar
lista.extend([6,7,8])
print(lista)

#se puede sumar concatenar dos listas
lista1 = [1,2,3]
lista2 = [6,7,8]
lista_total = lista1+ lista2

#determinar si hay un determinado elemento en la lista
lista_prueba = [1,2,3,4,"Alex"] * 2 #se  duplica la lista
print(3 in lista_prueba) #devuelve true o false dependiendo
#para saber en que posicion esta un elemento, tambien es sencillo
print(lista_prueba.index(4))

#En las listas puede haber valores repetidos. Luego si
#quiero saber cuantos repetidos hay e
#es tambien facil
lista_prueba = [1,2,3,4,4,"Alex"]
print(lista_prueba.count(4))

#Por ultimo, se aborda como eliminar elementos
lista_prueba.pop(0) #eliminamos elemento de la posicion 0
print(lista_prueba)

#con remove podemos eliminar sin tener la posicion
lista_prueba.remove("Alex")
#con clear borramos la lista entera
lista_prueba.clear()

#reverso de la lista
lista_prueba.reverse()
print(lista_prueba)

#ordenar la lista
numeros = [1,3,7,5,13,10]
numeros.sort()
print(numeros)
#ordenar de manera descente
numeros2 = [1,3,7,5,13,10]
numeros2.sort(reverse = True)
print(numeros2)
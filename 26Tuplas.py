'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 30-05-2020
    PROPÓSITO: MOSTRAR EL USO DE TUPLAS

    A diferencia de las listas, las tuplas son inmutables
    y son mas rapidas que las listas en el momento de ejecucion.
    Consumen mucha menos memoria que listas.
'''
tupla = (4, "Hola", 6.78, [2,3,4])
print(tupla)

#en la tupla no se puede adicionar ni quitar elementos

print(tupla[1])
print(tupla[1:]) #mostrar desde pos1 hasta final

#Busqueda tambien esta permitido
print(4 in tupla)

#Busqueda tambien es valida con el metodo index
#con index ,count..

#con metodo len nos indica el numero de elems en las tuplas
print(len(tupla))

#Se puede pasar de tupla a lista
lista = list(tupla)
print(f"La lista es {lista}")

#y se quiere pasar de lista a tupla
lista4 = [1,2,3,4]
tupla2 = tuple(lista4)
print(tupla2)
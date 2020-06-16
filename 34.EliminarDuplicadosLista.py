'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Eliminar elementos repetidos dela lista
'''

lista = [1,2,3,4,4,5] #primero se define la lista
#usar una coleccion que elimina los duplicados
conjunto = set(lista)
print(conjunto) #asi me quito los elementos repetidos
lista2 = list(conjunto)
print(lista2)

#y en una linea se puede tambian
ordenado = [1,2,3,3,3,3,4,5,6,6]
ordenado = list(set(ordenado))
print(f"El conjunto ordenado y sin repetidos es {ordenado}")


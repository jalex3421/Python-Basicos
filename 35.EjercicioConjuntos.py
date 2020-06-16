'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    *Escribir un programa que contenga dos listas, y se muestren
    *las siguientes listas:
    -lista de palabras que aparecen en las dos listas
    -lista qu palabras que aparecen en la primera lista, pero no en la segunda
    -lista de palabras que aparecen en la segunda, pero no en la primera
    -lista de palabras que aparecen en ambas listas
'''

#Lista de palabras que aparecen las dos listas
l1 = set()
l1 = {"Hola","Florida","DJ Snake"}
l2 = set()
l2= {"Hola","Martin Solveig","Evangelion","Rei"}
interseccion = list(l1.intersection(l2))
print(f"La interseccion es {interseccion}")
#lista de palabras que aparecen en la primera , pero no en la segunda
solo_primera = list(l1.difference(l2))
print(solo_primera)
#lista de palabras que aparecen en la segunda, pero no en la primera
solo_segunda = list(l2.difference(l1))
print(solo_segunda)
#lista de palabras que aparecen en ambas listas
#con ambas, me refiero a la union
ambas = list(l1.union(l2))
print(f"La union de ambas listas es : {ambas}")



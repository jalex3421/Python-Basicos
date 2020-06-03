'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 30-05-2020
    PROPÓSITO: MOSTRAR EL USO DE TUPLAS

   Grupo de elementos en los que no puede haber duplicados
   Repr. matemática: diagramas de Venn
'''

Conjunto = set() #si no ponemos esto, python cree que es diccionario

Conjunto = {1,2,3, "hola que tal",1,2,3}

print(Conjunto) #como se puede ver no se guardan los valores duplicados

#adicionar elementos : no respeta un orden
Conjunto.add(5) #no tiene por que agregarse al final
Conjunto.add("esto es un ejemplo") #no tiene por que agregarse al final
print(Conjunto)

#Eliminar elemento de un conjunto
#se pasa el elemento a eliminar
Conjunto.discard(3)

#En caso de querer vaciar el conjunto
Conjunto.clear()

#Buscar un determinado elemento
print(3 in Conjunto)
#Tambien puede devolver true si el valor no esta en el conjunto
print(3 not in Conjunto)

#ahora se veran algunos ejemplos mas de conjuntos
a = {1,2,3}
b= {3,4,5}
interseccion = a & b
print(f"El conjunto interseccion es {interseccion}")
print(f"La intersecciones {a.intersection(b)}")
#en la union se eliminan duplicados
c = a|b
print(f"El conjunto c es la union de los dos conjuntos: {c}")
print(f"La union de los dos conjuntos {a.union(b)}")
print(a==b) #testeamos si los dos conjuntos son iguales
print(f"El numero de elementos del conjunto a {len(a)}")
#para la diferencia
dif = a-b
print(f"La diferencia es {dif}")
print(f"La diferencia es {a.difference(b)}")
#diferencia simetrica
sim = a ^ b
print(sim)

#¿Como se determina si un conjunto es subconjunto de otro?
print(a.issubset(c)) #dara true, pues c contiene la union de a  y b
#¿Son los conjuntos disjuntos? Es decir, no tienen elementos en comun
print(a.isdisjoint(b))

#Conjuntos inmutables
Conjunto_inmutable = frozenset({1,2,3})
Conjunto_inmutable.add(3) #no se podra adicionar ningun elemento
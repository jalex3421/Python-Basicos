'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 30-05-2020
    PROPÓSITO: MOSTRAR EL USO DE PILAS

   Estructuras LIFO: ultimo en entrar, primero en salir
'''
#operamos las pilas, como si fuesen listas
pila = [1,2,3]
print(pila)

pila.append(4)
print(pila)

#sacar elementos: ultimo que entra, primero que sale
#pila.remove(len(pila))
cima = pila.pop()
print(pila)
print(cima)
#metodo pop, puede retornar elemento


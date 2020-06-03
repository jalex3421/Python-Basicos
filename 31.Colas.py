'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 30-05-2020
    PROPÓSITO: MOSTRAR EL USO DE COLAS

   Estructuras FIFO: ultimo en entrar, primero en salir
'''

cola = ["Maria", "Lucia", "Mario"]
print(cola)

#si llega alguien, al final
cola.append("Richard")
print(cola)

#ahora, el primero de la cola tras ser atendido, se va
primero = cola.pop(0)
print(f"La primera persona de la cola es : {primero}")
print(f"Tras atendender a Maria, quedan: {cola}")

#from collections import deque --> append, pop left
'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Introduccion al uso de ciclos, o bucles
'''

#¿Que ocurre si queremos sacar la raiz cuadrada de un numero?
#con el bucle while se tratara de sacar la raiz
import math
numero =(int)(input("Introduzca un numero:"))

#mientras no se cumple condicion, bucle se va iterando
while numero <0:
    numero = (int)(input("Introduzca un numero, esta vez posiivo:"))

print(f"La raiz cuadrada es {(math.sqrt(numero)):.2f}")

#segundo ejemplo
i = 0
while i<10:
    print("hola")
    print(f"Iteracion numero {i+1}")
    i+=1



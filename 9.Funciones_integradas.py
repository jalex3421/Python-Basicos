'''
    AUTOR: Alejandro Meza
    Fecha: 16-01-2020
    Proposito: FUNCIONES INTEGRADAS
'''

#sirven para hacer conversiones entre tipos de datos
n = float("10.8")
print(n)

#conversion de un numerico a cadena
n2 = str(10)
print(f"mi nueva cadena es {n2+str(1)}")

#conversion en binario
n3=bin(5565465465)
print(n3)
#Con int se puede pasar de binario a entero
binario= int("0b1010",2) #base 2
print("EL binario es: ",binario)

hexa= int("0xa",16)
print("El valor hexadecimal es: ",hexa)

#valor absoluto
n = abs(-8)

#round
n= round(5.6)
print(f"el redondeo es {n}")

#len: devuelve la longitud de la cadena
nombre= len("Alejandro")
print(f"La longitud del nombre es {nombre}")

#conversion en hex
n4 = hex(10)
print(n4)


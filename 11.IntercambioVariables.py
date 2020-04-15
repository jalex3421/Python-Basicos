'''
    AUTOR: Alejandro Meza Tudela
    FECHA: 17-01-2020
    Problema básico que intercambia valor de 2 variables
'''

a = (int)(input("Digite un valor: "))
b = (int)(input("Digite un valor: "))

'''
    aux = a
    a = b
    b = aux
'''

#aprovechandome de la sintaxis de python
a , b = b ,a

print(f"El valor de a cambiado es: {a}")
print(f"El valor de b cambiado es: {b}")



'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 18-01-2020
    PROPÓSITO: CAJERO AUTOMATICO
    1.INGRESAR DINERO
    2.RETIRAR DINERO
    3.MOSTRAR DINERO DISPONIBLE
    4.SALIR
'''

import sys

#saldo inicial de 1000 euros
saldo = 1000

print("\t.:MENU:.")
print("1.Ingresar dinero en la cuenta")
print("2.Retirar dinero de la cuenta")
print("3.Mostrar dinero disponible")
print("4.Salir")

opcion = (int)(input("Digite un numero de opcion de menu: "))
print()

if(opcion == 1):
    extra = (float)(input("Cuanto dinero desea ingresar -->"))
    saldo +=extra
    print(f"Dinero disponible en la cuenta es de {saldo}")
elif(opcion == 2):
    retirar = (float)(input("Cuanto dinero desea ingresar --> "))
    #el usuario no puede retirar mas de lo que tiene
    if(retirar > saldo):
        print("no se puede realizar operacion")
    else:
        saldo -= retirar
        print(f"Dinero disponible en la cuenta es de {saldo}")
elif(opcion == 3):
    print(f"Dinero disponible en la cuenta es de {saldo}")
elif(opcion == 4):
    print("Fin de uso de cajero")
    sys.exit(1)
else:
    print("error de opcion de menu")
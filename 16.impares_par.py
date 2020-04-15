'''
    AUTOR: Alejandro Meza Tudela
    FECHA: 18-01-2020
    Pedir 2 numeros y decir paridad
'''

def comprobador(numero1, numero2):
    if(numero1%2 == 0 and numero2%2!=0):
        print("El primer numero es par solo")
    elif(numero1%2 != 0 and numero2%2 ==0):
        print("El segundo numero es par solo")
    elif (numero1%2 == 0 and numero2%2 ==0):
        print("Los dos numeros son pares")
    else:
        print("ninguno es par")


num1 = (int)(input("Digite el primer numero: "))
num2= (int)(input("Digite el segundo numero: "))

comprobador(num1, num2)

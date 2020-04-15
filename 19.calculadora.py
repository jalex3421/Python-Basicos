'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 18-01-2020
    PROPÓSITO: CALCULADORA
'''


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2





print("..............................................")
print("BIENVENIDO A LA CALCULADORA")
print("s: suma, r: resta, m:multiplicacion, d: division")
operacion = input("Introduce s,r, m o d dependiendo de lo que hagas:").upper()
num1 = (float)(input("introduce el numero 1:"))
num2 = (float)(input("Introduce el numero 2: "))
print("..............................................")

if operacion == 'S':
    res = suma(num1, num2)
    print(f"\nLa suma es {res}")
elif operacion == 'R':
    res = resta(num1,num2)
    print(f"\nLa resta es {res}")
elif operacion == 'M':
    res = mult(num1, num2)
    print(f"\nLa multiplicacion es {res}")
elif operacion == 'D':
    res = div(num1, num2)
    print(f"\nLa division es {res}")
else:
    print("\nSe equivoco de operacion")



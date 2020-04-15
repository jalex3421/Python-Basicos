'''
    AUTOR: Alejandro Meza Tudela
    FECHA: 18-01-2020
    Determina el mayor de 3
'''

#pedir 3 numeros y determinar el mayor


#se puede usar and y acortas codigo
def mayor(n1, n2, n3):
    if(n1>n2):
        if(n1>n3):
            print(f"El mayor es{n1}")
        elif(n1<n3):
            print(f"El mayor es {n3}")
    elif(n2>n1):
        if (n2 > n3):
            print(f"El mayor es{n2}")
        elif (n2 < n3):
            print(f"El mayor es {n3}")
    elif(n3>n1):
        if(n3>n2):
            print(f"El mayor es {n3}")
        elif(n3<n2):
            print(f"El mayor es {n2}")

num1 = (int)(input("Introduce numero1: "))
num2 = (int)(input("Introduce numero1: "))
num3 = (int)(input("Introduce numero1: "))

mayor(num1, num2, num3)
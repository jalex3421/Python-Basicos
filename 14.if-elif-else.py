'''
    AUTOR: ALEJANDRO MEZA
    FECHA: 17-01-2020
    CONDICIONALES
'''

#condicionales

def calificador(input):
    if(input>0):
        print("el numero es positivo")
    elif(input<0):
        print("El numero es negativo")


def calificador_extra(input):
    if(input>0):
        print("jejejeje")
    elif(input == 0):
        print("es 0 el numero introducido")
    else:
        print("jajajajaja")

numero = (int)(input("Introduce un numero: "))

calificador(numero)
calificador_extra(numero)

print("fin del programa")
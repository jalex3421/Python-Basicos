'''
    AUTOR: Alejandro Meza
    FECHA: 17-01-2020
    Mas de condicionales
'''

#condicionales combinados
#no existe el switch en python

def comprobador(input):
    #se combinan los condicionales
    #if(input>0 and input<110):
    if 0<input<110:
        print("edad valida")
        if(input>=18):
            print("La persona es mayor de edad")
            print(f"Tiene {input} años")
        else:
            print("la persona no es mayor de edad")
    else:
        print("La edad de entrada no es correcta")

edad = (int)(input("Digite su edad:"))

comprobador(edad)
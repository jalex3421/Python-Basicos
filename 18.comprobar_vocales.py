'''
    Pedir caracter e indicar si es vocal o no
'''

#cuidado con las mayusculas .lower()
#caracter = caracter.lower()
caracter = (input("Digite un caracter: ")).lower()

if(caracter == 'a' or caracter == 'e' or caracter== 'i'
 or caracter == 'o' or caracter == 'u'):
    print("El caracter es una vocal")
else:
    print("El caracter introducido no es una vocal")
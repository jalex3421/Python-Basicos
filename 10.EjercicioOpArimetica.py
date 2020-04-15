'''
    EJERCICIO 1:


a = (int)(input("introduce el primer numero: "))
b = (int)(input("introduce el segundo numero: "))
c = (int)(input("introduce el tercer numero: "))

expresion = ((a**3)*(b**2 - 2*(a*c)))/(2*b)
print(f"La evaluacion de la expresion es {expresion}")
'''

'''
    EJERCICIO 2:
'''
a = (float)(input("introduce el primer numero: "))
b = (float)(input("introduce el segundo numero: "))

resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
#evalua los parentesis mas internos primeros
#se evalua primero la multiplicacion
#luego la division y la multiplicacion
#por ultimo el ultimo parentesis: el de la derecha...
#se repite lo mismo otras veces
print(f"El resultado es: {resultado}")


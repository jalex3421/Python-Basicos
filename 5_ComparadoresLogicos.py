'''
    AUTOR: Alejandro Meza Tudela
    FECHA: 15-01-2019
    OPERADORES LOGICOS: algebra de bool
                        Permiten construir operaciones lógicas
                        And, or y not
    PRECEDENCIA: NOT, AND, OR
'''

#Operacion AND
#se evalua como algebra de bool
#multiplicacion logica: 0 y 1

val1 = True
val2 = True
print(val1 and val2)

#Operacion OR
#Suma Logica: sigue lo mismo que el algebra de bool
val1 = True
val2 = False
print(val1 or val2)

#Operacion not: invierte los resultados obtenidos
a = 10
b = 12
c = 13
d = 10
resultado = ((a>b)or(a<c))and((a==c)or(a>=b))
print("La evaluacion final es: ",resultado)
#  f    or   t         f       f
#     t        and          f
#fin: false



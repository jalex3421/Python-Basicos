'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Introduccion al uso de bucles for
'''

#los bucles for se usan con colecciones
lista =[1,2,3,4,5] #esta es la coleccion  con la que se va a tratar
for i in lista:
    print("hola , que tal") #iterará 5 veces, una vez por cada elemento
    #recorre elemento a elemento, los elementos de la coleccion
    print(f"el valor de la iteracion es: {i}")

coleccion = {"Alejandro" : 20, "Nerea" : 21}
for i in coleccion:
    print(f"La clave es:  {i}")
    print(f"El valor es: {coleccion[i]}")
    print(f"{i} con edad de : {coleccion[i]}")

#ahora probemos un for, con dos variables
#definimos tambien un diccionario
personas = {"Henry" : 38, "Humberto" : 50, "Inigo" : 24 }
for clave, valor in personas.items(): #con items se recorr. elems de diccionario
    print(f"{clave} --> {valor}")
#recorrer cadenas
cadena = "hola"
#por defecto, la funcion print aniade un salto de linea
#por eso con 'end', se puede modificar la terminacion
for i in cadena:
    print(f"{i}",end = " ")
#puede aniadirse un range, para iterar tantas veces como se quiere





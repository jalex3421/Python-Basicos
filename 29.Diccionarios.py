'''
    AUTOR: ALEJANDRO MEZA TUDELA
    FECHA: 30-05-2020
    PROPÓSITO: MOSTRAR EL USO DE DICCIONARIOS

   Cada elemento tiene dos valores por posicion: la clave
    y el valor
'''
               #clave  valor   clave   valor
diccionario = {"azul":"blue","rojo" : "red"} #diccionario vacio
print(diccionario["azul"])

#agregar nuevos elementos --> no se agregan con orden
diccionario["amarillo"] = "yellow"
print(diccionario)
#modificar
diccionario["azul"] ="BLUE"
#para eliminar un valor
del(diccionario["azul"]) #eliminamos clave verde y su valor

agenda = {"Alejandro": {20,1.70}}
print(agenda["Alejandro"])

#clave de tipo entero, y valor es una cadena
equipo = {10:"Paulo Dybala", 11: "Douglas Costa", 7: "Cristiano Ronaldo"}
print(equipo[10]) #imprime el jugador que posea dicha clave
#print(equipo[6]): key error; pues no se encuentra clave dentro de diccionario
print(equipo.get(6, "no existe"))
#mostrar solo claves de diccionario
print(equipo.keys()) #muestra dentro de una lista, las claves del diccionario
print(equipo.values()) #muestra valores, no claves
#se quiere saber cuantos elementos
print(len(equipo))
#borrar un diccionario
equipo.clear()
print(equipo)
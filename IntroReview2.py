'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Little introduction of Python part 2
'''

#Tuples
#tuples are inmutable versions of lists
my_tuple = (1,2,3)
print(my_tuple[1:])
one_element_tuple = (2,)
print(one_element_tuple)
#in order to obtain the index of an element --> index
print(f"The position of the number 1 is {my_tuple.index(1)}")
print(f"Number 1 appears {my_tuple.count(1)} times")

#SLICING : play with the indexes
silicon_valley = ["Richard", "Gilfoyle", "jared", "Erlich"]

print(silicon_valley[0])
print(silicon_valley[1:3]) # 1, n-1
print(silicon_valley[2:]) # positions 2 and 3
#(start, end , inc)
print(silicon_valley[0:3:2]) # from 0 to 3, increment by 2

#DICTIONARIES
#also called HASH MAPS (like java) or associative array
#set of key-value pairs
#mutables           #clave   valor ||      clave: valor
bayern = {1: "Neuer", 25: "Thomas Muller", 32: "Mario Gomez"}
print(bayern[1].__getitem__(1)) #obtaint 'e' from 'Neuer'
print(bayern.items())
print(bayern[32])
#we could change players, for example:
bayern[32] = "Mario Mandzuckich"
print(bayern[32])
#then, if we want to transfer one player to other team,
#we are simply capable of delete the player from our team
del(bayern[32])#we show the key that we want to delete
print(bayern.items())
#if we want to add an element, the idea is
#to add a pair key-value with a key that it does not exist
bayern[10] = "Robben"
print(f"Our new dictionary is {bayern.items()}")
#we can show only the keys
print(f"The numbers of shirts from our players is {bayern.keys()}")
#with the same idea, we can only show the value
print(f"the name of the players are {bayern.values()}")

#DATA TYPE SUMMARY
#integers, floating point, complex: 3 + 2j
#lists = [1,2,3]
#sets s = {1,2,3}
#tuples t = (1,2,3)
#dictionaries d = {10 : 'Robben', 25: 'Thomas Muller'}

#INPUT
#we can use ideas like putting (int) or (float) at the beginning
#of the

'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Little introduction of Python part 1
'''

#Everything in Python is an object. Data type is a property
#of the object and not of the variable

#Math commands
#abs(value), log(value), log10(value), max(val1, val2),
#min(val1, val2), round(value), sin(value), sqrt(value)
#constant --> e and pi
import math
x = -1
y = 2
mi_valor_pi = 3.14
ang1 = 90
number = 64

print(math.fabs(x))
print(math.log(2,2))
print(max(x,y))
print(f"The minvalue is : {min(x,y)}")
print(f"The value of pi rounded is  : {round(mi_valor_pi)}")
print(f"The sinus of my value is : {math.sin(ang1)}")
print(f"the value of the squareroot is:  {math.sqrt(number)}")

#Booleans
#0 and None --> false
#eveything --> True
#True: 1 and False : 0
#AND and OR return one of the elements in the expression
print(True and False) #--> F

#STRING LITERALS
#'+' is overload to do concatenation
pal1 = 'hello'
pal2 = ' world'
print(pal1+pal2)
#''' is usefull for a multi-line string
s = ''' Hi, my name is Alex and i like to code 
      in my freetime. I love java and python, but C
       is my favourite
     '''
print(s)
#len(s) return an integer which is the length of my word
#str(object) return a string representation of the object
pal3 = '012345'
print(f"the values from 1 to 4 are: {pal3[1:4]}")
print(f"The length of the word hello is {len(pal1)}")
print(f"A string representation of a number could be: {str(3.14)}")
#let x be an string variable
#x.lower, x.capitalize, x.upper, x.count, x.find
#x.startswith , x.endswith, x.isalnum
x = 'proof'
print(x.capitalize())
print(x.upper())
#string, formatting
print("One, %d , three" %2)
print("I have %d %s" % (4, 'dogs'))

#LISTS
#list could contain objects from different types
lista = [1, "hello", (3+2j)]
print(lista[2])
#in order to modify content, we could follow some strategies
lista.append(3)
print(lista)
lista.remove(3)
print(lista)
lista.pop() #delete the last element, like a stack
print(lista)
#other form to add elements, is following the next idea:
lista += [4,5,6]
print(lista)
#sort, range, append, reverse, extend, remove
#ZIP two list together, with the funcion called zip
#list = zip(l1, l2)

#we can also create lists using math expressions
#create a list with number^2 between 0 and 9
s = [x**2 for x in range (10)]
print(s)

#create a list, which starts with 1 and finish in 4096
#but all the numbers follow the form 2^x
v = [2**x for x in range (13)]
#in the expression the x could have the values: 0 ... 12 (13 values)
print(v)

#we can also have the same impact with functions like 'map', for
#example

#list which starts from strings
quot = 'i like pizza'.split()
print(quot)
#with this idea, we can also manipulate each word in the sentence
#print([word.upper(), word.lower(), word.upper()]for word in quot)

#Generate a list composed of 3 list having 5 elements. Each element
#should be a touple like that --> (i,j)
l = [] #main list for our operations
for i in range(3): #iterate three times for our sublist
    laux = []    # a sublist
    for j in range(5): #5 elements in the list
        laux.append((i,j))
        #add the number of the iteration and the element(0-4)
    l.append(laux)
print(l)

#SETS
#Unordered collections of unique elements
#they cannot contain mutable elements such as list or dicitonaries
set1= set()
set1 = {1,2,3}
print(set1)
set2 = set()
set2 = {3,4,5}
print(f"The common element is {set1.intersection(set2)}")
#Operations: len(s), x in s, x not in s, s.issubset(t)
#s.union(s2) , s1.intersection(s2), s1.difference(s2)
#s.copy(), s.symetic_diferecbce(s2)


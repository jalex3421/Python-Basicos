'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Little introduction of Python part 3
'''

import math

#INPUT
#we can use ideas like putting (int) or (float) at the beginning
#of the input. Now we are going to look at some examples
'''
print("What's your name dude ? : ")
name = input(">")
print("And what's your age? : ")
age = (int)(input(">"))
print(f"So your age is {age} and your name is {name}")
'''

#FILES INPUT
#inflobj = open('data', 'r') open the file data for input
#s = inflobj.read() read whole file into one String
#s = inflobj.read(N) --> read N bytes
#L = inflobj.readlines(): Returns a list of line strings

'''
inflobj = open('quijote.txt', 'r')
my_string = inflobj.read()
#print(my_string) --> we are able to print the book
N = 1024
my_string_N_bytes = inflobj.read(N)
print(my_string_N_bytes)
#we are going to captura all the text in a common list
my_list = inflobj.readlines()
inflobj.close()

'''


#FILES OUTPUT
'''
outflobj = open('quijote.txt', 'w') #open the data for writing
S = 'esto es un adicional'
#outflobj.write(S) #se escribe en el texto 
#      --> pero no se adiciona al final de este, sino se sustituye 
#L = ['hello', 'world']
#outflobj.writelines(L) #write each of the strings in L to the file
outflobj.close() #close the file
'''

#In general terms the idea is the following:

'''
FOR READING FILES:
fin = open('filename', 'r')
for line in fin:
     #manipulate the line
fin.close()
'''
#APPEND text instead of replace it
#fin = open('quijote.txt','a')
#fin.write('Evangelion is a fantastic anime for us')
#fin.close()

'''
FOR WRITING FILES:
fout = open('filename', 'w')
fout.write('Sentence'
fout.close() 
'''

#IF STATEMENTS

x = 30
y = 0
if x <15:
    y = x+15
else:
    y = -x
print(math.sin(y))

#AND | OR | NOT
if x<-4 or x > 4:
    print("that's true mate")
#chained comparisons
if 3<x<33:
    print("This is our correct range")

#FOR LOOOPS
def clean_output():
    print()
    print()
#ALTERNATIVE 1
list_a = [1,2,3]
for i in list_a:
    print(i)
clean_output()
#ALTERNATIVE 2: set a normal range
# --> i = 0 .....   i = 9
for i in range(10):
    print(i)
#Loops control statements
#break
#continue --> jumps to the top of the closest encolsing loop
#pass --> does nothing
#example of break
clean_output()
for i in range(10):
    print(i)
    if(i == 6):
        print("I exit the loop")
        break
#example of continue
clean_output()
for i in range(5):
    print(i)
    if(i == 4):
        continue
#WHILE + else
#if i have an else instruction, it will run after the
#loop exist normally --> not breaks instructions
clean_output()
x = 1
while(x<3):
    print(x)
    x+=1
else:
    print("Well, the loop has finished")
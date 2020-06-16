'''
    Autor: Alejandro Meza
    Fecha: 01-06-2020
    Little introduction of Python part 4
'''

#FUNCTION BASICS
def max (x,y):
    if(x >y):
        return x
    else:
        return y

x = (int)(input("Introduce x: "))
y = (int)(input("Introduce y: "))
print(f"The maxVal is {max(x,y)}")
#also we can assign the result to a variable
my_var = max(x,y)
print(f''' The result is the same
   but with one variable {my_var}
''')

#another example of calling a function in order to use it
def foo(a,b,c):
    print(a,b,c)
foo(a = 4, b = 3, c = 6)

#Using function as parameter
def printer(f,a):
    return f(a) # we apply the function to the parameter
     #that we give to the function printer

def cuadratic(x):
    return x*x
print( printer(cuadratic, 3))

#functions could be inside others functions

#Anonymous functions: lambda
#   ONLY simple expressions --> not complex statements
f = lambda x,y : x+y
print(f(4,7))

#higher-order functions
#map(func, seq) for al elements i applies the function i
# --> func(seq[i])
def double(x):
    return 2*x
lst = range(10)
#print(map(double, lst)) --> the idea is to apply our function in all the elements
#from our list


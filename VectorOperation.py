'''
Author: Alejandro Meza Tudela
    Simulate the action of taking from input
    values to a vector that is declared
'''

def clean_screen():
    print()

vector = list()
len_vector = (int)(input("Enter the number of elements of the vector: "))
clean_screen()
print("Now, enter the elements for the vector: ")
for i in range(len_vector):
    elem = (int)(input(f"elem {i+1}: "))
    vector.append(elem)
clean_screen()
print(f"The vector is {vector}")

# Mutable Vs Immutable Data Types :

# List, Tuple, Set, Dictionary

# String, Integer, Float, Boolean 

# User Defined Data Types : 
# Primitive Data Types : 


full_name = 'Sagar Thapa' 
address = "Baneshwor, Kathmandu"
country = str('Nepal') 

# 
# New value stored in the same variable name but diffrent memory location
# full_name = "Agar Thapa" 

# print(full_name)

# String indexing , slicing
# print(full_name[0]) # Indexing
# print(full_name[1]) # Indexing
# print(full_name[2])
# print(full_name[3])
# print(full_name[4])
# print(full_name[5])
# print(full_name[6])
# print(full_name[7])
# print(full_name[8])
# print(full_name[9])

# print(full_name[-2:-1])

# String Concatenation

# first_name = "Sagar"
# last_name = "Thapa"

# first_name = input("Enter your first name \n")
# last_name = input("Enter your last name \n")

# name = first_name + " " + last_name
# print(name)

# print("First Name Is " + first_name, "\n",  "Last Name Is " + last_name)

# String Formatting .format vs f strings

# print(f"First name is {first_name} and last name is {last_name}")

# # Using arguments
# print("First name is {} and last name is {}".format(first_name, last_name))

# # Using Keyword arguments
# print("First name is {a} and last name is {b}".format(a=first_name, b=last_name))

# # Using args, kwargs
# print("First name is {} and last name is {b}".format(first_name, b=last_name))






# Integer


# num_1 = 10
# num_2 = 2.2

# # print(f"NUM 1 : {num_1} and NUM 2 : {num_2}")


# # num_3 = int(1.123) # Type casting 

# # print(f"The type casted value is {num_3}")


# # Operators and operations in numbers

# # +, -, *, / , %


# sum_of_numbers = num_1 + num_2
# sum_of_numbers = sum([num_1, num_2]) # Sum func

# diff_of_numbers = num_1 - num_2

# mul_of_numbers = num_1 * num_2

# div_of_numbers = num_1 / num_2 

# fdiv_of_numbers = num_1 // num_2 

# mod_of_numbers = num_2 % num_1


# # DocString 
# print(
#     f"""
#     Sum : {sum_of_numbers}
#     DIFF : {diff_of_numbers}
#     MUL : {mul_of_numbers}
#     DIV : {div_of_numbers}
#     FDIV : {fdiv_of_numbers}
#     MOD : {mod_of_numbers}
#     """
# )





# num_1 = input("Enter any number \n")
# num_2 = input("Enter any number \n")


# # num_1 = int(num_1)
# # num_2 = int(num_2)

# # print(f"Sum of two numbers is {num_1 + num_2}")
# if num_1.isnumeric() and num_2.isnumeric():
#     breakpoint()
#     num_1 = int(num_1)
#     num_2 = int(num_2)

#     print(f"Sum of two numbers is {num_1 + num_2}")
# else:
#     print(f"""Cannot do operation in non numeric values N1: {num_1} , N2 : {num_2}""")



# bv = bool({1123}) # True, or False
# print(f"O/P is {bv}")



# List [], Tuple (), Set {}, Dictionary {}




students_tuple = ('Ram', 'Shyam', 'Rita', 'Hari') # () or tuple()
students_set = {'Ram', 'Shyam', 'Rita', 'Hari'} # {} or set()
student = {
    "name" : "Ram",
    "age": 12,
    "address": "Mid Baneshwor",
    "parent_name" : "Dasarath",
}


students_list = ['Ram', 'Shyam', 'Rita', 'Hari'] # [] or list()
# Inserting items to list
students_list.append("Aagaman")
students_list.append("Sunita")

# Removing items to list
students_list.pop(0)
students_list.remove("Sunita")

# Loops in python

# for , while

# for value in students_list:
#     print(value)


# for index, value in enumerate(students_list):
#     print(index, value)


# for i in range(99):
#     print(f"Printing for {i}")


# write a program to
# scan 5 students name from terminal, insert the names into list and display them


"""
students = []

for i in range(5):

    name = input("Enter name of student \n")

    students.append(name)

print(students)
"""


# roll_numbers = {0,0,1,1,2,2,2,3,3,3,3,4,5,6,7}

# breakpoint()
# print(roll_numbers)



# write a program to
# scan 10 students name from terminal, add the names into set and display them



# students = []

# for i in range(10): students.append(input("Enter name \n"))

# print(students)

# breakpoint()




student = {
    "name" : "Ram",
    "age": 12,
    "address": "Mid Baneshwor",
    "parent_name" : "Dasarath",
}
student.keys()
student.values()
student.items() 
student.update(new_key='NEW VALUE')
student['new_key_1'] = 'New Value 1'

# # (Pdb) student   
# {'name': 'Ram', 'age': 12, 'address': 'Mid Baneshwor', 'parent_name': 'Dasarath'}
# # (Pdb) student.keys()
# dict_keys(['name', 'age', 'address', 'parent_name'])
# # (Pdb) student.values()
# dict_values(['Ram', 12, 'Mid Baneshwor', 'Dasarath'])
# # (Pdb) student.items() 
# dict_items([('name', 'Ram'), ('age', 12), ('address', 'Mid Baneshwor'), ('parent_name', 'Dasarath')])
# # (Pdb) student.update(new_key='NEW VALUE')
# # (Pdb) student.items()
# dict_items([('name', 'Ram'), ('age', 12), ('address', 'Mid Baneshwor'), ('parent_name', 'Dasarath'), ('new_key', 'NEW VALUE')])
# # (Pdb) student['new_key_1'] = 'New Value 1'
# # (Pdb) student.items()
# dict_items([('name', 'Ram'), ('age', 12), ('address', 'Mid Baneshwor'), ('parent_name', 'Dasarath'), ('new_key', 'NEW VALUE'), ('new_key_1', 'New Value 1')])

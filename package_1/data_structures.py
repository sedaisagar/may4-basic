# # Dictionary

# person = {} or dict()
# # Key value pair
# person.setdefault("name", "Sagar Sedai") # 
# print("Name Key Present",person)

# person["name"] = "Laxmi Kathayat" # Changes the value of that key if present
# person["age"] = 20 # Changes the value of that key if present
# print("Name key is present", person)

# person.update(
#     name = "Aabhiyan Karki",
#     age = 30,
#     address = "Hetauda"
# ) #  changes
# print("Name's value is updated",person)

# print("-"*50)

# name = person.get("name", "No name")
# age = person.get("age", "No age")
# address = person.get("address", "No address")

# # name = person.pop("name", "No name")
# # age = person.pop("age", "No age")
# # address = person.pop("address", "No address")

# # name = person["name"]
# # age = person["age"]
# # address = person["address"] # This causes exception

# print(name, age, address, "\n", "-"*50)

# print(person)

# for i in person.keys():
#     print(i, person[i])
#     print(i, person.get(i))
#     # print(i, person.pop(i))



# # WAP to 
# # Create an empty dict with name student
# # ask for student name, age, address, grade, section from terminal
# # add those keys with value in dict
# # and finally print that dictionary


# student = {}

# name = input("Enter name \n")
# age = input("Enter age \n")
# address = input("Enter address \n")
# grade = input("Enter grade \n")
# section = input("Enter section \n")


# student.update(
#     name = name,
#     age = age,
#     address = address,
#     grade = grade,
#     section = section,
# )

# print(
#     f"""
#     {student}
#     ----------------
#     Name : {student.get("name")}
#     Age : {student.get("age")}
#     Address : {student.get("address")}
#     Grade : {student.get("grade")}
#     Section : {student.get("section")}
#     ----------------
#     """
# )

# List

# students = []
students = [
    {'name': 'B', 'age': '13', 'address': 'asd', 'grade': 'asd', 'section': 'asd'},
    {'name': 'D', 'age': '17', 'address': 'ads', 'grade': 's', 'section': 's'}, 
    {'name': 'G', 'age': '16', 'address': 'sad', 'grade': 'sda', 'section': 'sd'}, 
    {'name': 'J', 'age': '11', 'address': 'asd', 'grade': 'sd', 'section': 'sda'},
    {'name': 'A', 'age': '12', 'address': 'asdfasdf', 'grade': 'asdf', 'section': 'asd'}, 
]

# for i in range(5):
    
#     student = {}

#     name = input("Enter name \n")
#     age = input("Enter age \n")
#     address = input("Enter address \n")
#     grade = input("Enter grade \n")
#     section = input("Enter section \n")


#     student.update(
#         name = name,
#         age = age,
#         address = address,
#         grade = grade,
#         section = section,
#     ) 

#     students.append(student)

students.insert(100, {'name': 'E', 'age': '14', 'address': 'asdfasdf', 'grade': 'asdf', 'section': 'asd'}, )

print(students) 
print("-"*50)
students.sort(key=lambda x: x.get("age"), reverse=True)
print(students) 





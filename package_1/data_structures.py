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
# students = [
#     {'name': 'B', 'age': '13', 'address': 'asd', 'grade': 'asd', 'section': 'asd'},
#     {'name': 'D', 'age': '17', 'address': 'ads', 'grade': 's', 'section': 's'}, 
#     {'name': 'G', 'age': '16', 'address': 'sad', 'grade': 'sda', 'section': 'sd'}, 
#     {'name': 'J', 'age': '11', 'address': 'asd', 'grade': 'sd', 'section': 'sda'},
#     {'name': 'A', 'age': '12', 'address': 'asdfasdf', 'grade': 'asdf', 'section': 'asd'}, 
# ]

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

# students.insert(100, {'name': 'E', 'age': '14', 'address': 'asdfasdf', 'grade': 'asdf', 'section': 'asd'}, )

# print(students) 
# print("-"*50)
# students.sort(key=lambda x: x.get("age"), reverse=True)
# sorted_students = sorted(students, key=lambda x: x.get("age"), reverse=True)
# print(students) 
# print(sorted_students) 


# MAP, SORTED, FILTER, COMPREHENSION

# Map is a func, that transforms data in a list

# students = [
#     {'name': 'B', 'age': '13', 'address': 'asd', 'grade': 'asd', 'section': 'asd'},
#     {'name': 'D', 'age': '17', 'address': 'ads', 'grade': 's', 'section': 's'}, 
#     {'name': 'G', 'age': '16', 'address': 'sad', 'grade': 'sda', 'section': 'sd'}, 
#     {'name': 'J', 'age': '11', 'address': 'asd', 'grade': 'sd', 'section': 'sda'},
#     {'name': 'A', 'age': '12', 'address': 'asdfasdf', 'grade': 'asdf', 'section': 'asd'}, 
# ]

# transformed_students = list(map(lambda x : {"age":x.get("age")}, students))
# print(transformed_students)

# min_age = 15
# filtered_students = list(filter(lambda x : int(x.get("age")) >= min_age, students))

# print(filtered_students)


# Write a python program to

# Product Management
# Scan for 5 items (products) from terminal
# Product (name, category, price, stock_qty)
    # name , category => str
    # price => float, stock_qty => positive integer

# 0. Filter products that are in stock (stock_qty > 0)
# 1. Sort first on the basis of price descending
# 2. Sort second on the basis of name ascending
# 3. Map the whole dict in string like "Watch - Wearable - 500" 




products = [
    {
        "name": input("Enter name of product \t"),
        "category": input("Enter product category \t"),
        "price": float(input("Enter product price \t")),
        "stock_qty": int(input("Enter stock quantity \t")),
    } for _ in range(5)
]

print("="*50)

filtered_products = list(filter(lambda x : x["stock_qty"] > 0 , products))

sorted_first  = sorted(products, key=lambda x: x["price"], reverse=True)

sorted_second  = sorted(products, key=lambda x: x["name"], reverse=False)

mapped_products = list(map(lambda x: f"{x["name"]} - {x["category"]} - {x["price"]}", products))

print(filtered_products)
print("="*50)
print(sorted_first)
print("="*50)
print(sorted_second)
print("="*50)
print(mapped_products)
print("="*50)

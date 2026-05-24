# Class Definition

class Person:
    # attributes and methods
    
    # public, private, protected

    name = ""
    # address = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        
        for k,v in kwargs.items():
            setattr(self, k, v)
            # if hasattr(self, k):
            # else:
            #     print(f"Attribute {k} does not exist in the class.")

    def greet(self):
        print(f"Hello, my name is {self.name}.")
    
    def talk(self):
        print(f"Hello, my name is {self.name}.")

    

# instance = Person(1,2,3,4,name="Sagar", age=30, city="Kathmandu")

# # instance.name = "Sagar"
# instance.greet()


# Write a program in python
# Create a class Student with attributes name, age, grade. 
# Set the attributes using the constructor.
# Create a method called display_info that prints the student's information.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-------------")

# # Student first
# student1 = Student("Alice", 20, "A")
# student1.display_info()

# # Student second
# stdemt2 = Student("Bob", 22, "B")
# stdemt2.display_info()

# Inheritance: single, multiple, and multi-level

class Education:
    edu_degree = "No degree"
    edu_marks = "No marks"
    
    __year = 2020 # This is private property


    def display(self):
        print(f"Education display method {self.__year}")

class Parent(Education):
    name = "No name"
    height = "No height"

    _religion = "Super secret religion"

    def display(self):
        print("Parent display method")
        super().display()

class Child(Parent): 
    hobby = "No hobby"

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    # Overriding the display method
    def display(self):
        print(f"""
            --------- Child display method ---------
                Name: {self.name}
                Height: {self.height}
                Education Degree: {self.edu_degree}
                Education Marks: {self.edu_marks}
                Hobby: {self.hobby}
                Religion : {self._religion}
            ---------------------------------------       
        """)
        super().display()

child_instance = Child(name = "Sagar", height="6 feet", edu_degree = "Engineering",edu_marks = "74", hobby="Dev")
child_instance.display()
print(Child.__mro__)
breakpoint()

# MRO : Method Resolution Order

# Create a mini banking system in python using OOP concepts.

# 1. Create a class BankAccount with attributes account_number, account_holder, balance.
# 2. Use Encapsulation to make the balance attribute private and provide methods to deposit, withdraw, and check balance.
# 3. Create a subclass SavingsAccount that inherits from BankAccount and add an attribute interest_rate. Implement a method to calculate interest. 
# 4. Create another subclass CurrentAccount that inherits from BankAccount and add an attribute overdraft_limit. 
# 4.1. Implement a method to check if the account is overdrawn.
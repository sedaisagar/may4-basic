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

    

instance = Person(1,2,3,4,name="Sagar", age=30, city="Kathmandu")

# instance.name = "Sagar"
instance.greet()


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

# Create a mini banking system in python using OOP concepts. 
# 1. Create a class BankAccount with attributes account_number, account_holder, balance.
# 2. Use Encapsulation to make the balance attribute private and provide methods to deposit, withdraw, and check balance.
# 3. Create a subclass SavingsAccount that inherits from BankAccount and add an attribute interest_rate. Implement a method to calculate interest.
# 4. Create another subclass CurrentAccount that inherits from BankAccount and add an attribute overdraft_limit.
# 4.1. Implement a method to check if the account is overdrawn


class BankAccount:
    account_number, account_holder, __balance = "", "", 0

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder

    def deposit(self, amount):
        self.__balance += amount
        self.check_balance()

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print(f"Insufficient fund to withdraw, available balance is {self.__balance}")
            # raise ValueError()
        self.check_balance()

    def check_balance(self):
        print(f"Current balance is {self.__balance}")
        print("="*50, "\n")
    
    @property
    def get_balance(self):
        return self.__balance
class SavingsAccount(BankAccount):
    interest_rate = 0

    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance * self.interest_rate / 100
        print(f"The earned interest is {interest}")

# bank_instance = BankAccount("555088526525", "Ram Hari Pandey")
# bank_instance.deposit(50000)
# bank_instance.withdraw(70000)
# bank_instance.check_balance()

savingacc_instance = SavingsAccount("555088526525", "Ram Hari Pandey", 5)
savingacc_instance.deposit(50000)
# savingacc_instance.withdraw(70000)
savingacc_instance.calculate_interest()

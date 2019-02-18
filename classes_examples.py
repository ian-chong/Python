class BankAccount():
    def __init__(self, balance, client_name):
        self.balance = balance
        self.client_name = client_name

    def deposit(self, balance):
        self.balance = self.balance + balance
    
john_bank_account = BankAccount(100, "John Feruni") # create a BankAccount instance
print(type(john_bank_account)) # print out what type john_bank_account is; should yield `<class '__main__.BankAccount'>`
print(john_bank_account.balance) # retrieve balance attribute for john_bank_account
print(john_bank_account.client_name) # retrieve client_name attribute for john_bank_account

sam_bank_account = BankAccount(200, "Samantha Feruni")
print(type(sam_bank_account))
print(sam_bank_account.balance)
print(sam_bank_account.client_name)


# class Dog():
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#         self.species = 'mammals'

# daisy = Dog('Shih Tzu', 'Daisy')

# print(daisy.name)
# print(daisy.breed)
# print(daisy.species)

class Animal():
    def __init__(self, food):
        self.food = food
        print('Animal Created')
        # yes! __init__ maybe a special method but when writing logic for it, treat it just like any other methods. You would usually write any initializing code in here.

    def feed(self):
        print(f"Feeding {self.food}")

class Dog(Animal):
    def __init__(self, breed, name, food):
        Animal.__init__(self, food) # call the parent class' `__init__` method as well
        self.breed = breed
        self.name = name

    def walk(self):
        print(f"Walking {self.name}")
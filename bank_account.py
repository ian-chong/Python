class BankAccount():
    def __init__(self, balance, client_name, account_number):
        self.balance = balance
        self.client_name = client_name
        self.account_number = account_number

    def deposit(self, balance):
        self.balance = self.balance + balance
        print (self.balance)

    def withdraw(self, balance):
        self.balance = self.balance - balance
        print (self.balance)

    def transfer(self, receiver, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            receiver.balance = receiver.balance + amount
        
        elif self.balance < amount:
            print ("You do not have enough cash")

ian_bank_account = BankAccount(500, "Ian", 10001)
pris_bank_account = BankAccount(2000, "Pris", 10002)


ian_bank_account.balance
pris_bank_account.balance
print (ian_bank_account.balance)
print (pris_bank_account.balance)

pris_bank_account.transfer(ian_bank_account, 5000)
print (ian_bank_account.balance)
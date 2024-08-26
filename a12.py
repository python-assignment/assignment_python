'''1. Write a Python program to create a class representing a shopping cart.
 Include methods for adding and removing items, and calculating the total price.'''

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity):
        self.items.append({'name':item_name, 'price':price, 'quantity':quantity})

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item ['name']!= item_name]

    def calculate_total(self):
        return sum(item['price'] * item ['quantity'] for item in self.items)

cart = ShoppingCart()
cart.add_item('Banana', 10, 3)
cart.add_item('orange', 5, 6)
print("Total price", cart.calculate_total())
cart.remove_item('Banana')
print("Total price after removing Banana", cart.calculate_total())


'''2. Write a Python program to create a class representing a bank. 
Include methods for managing customer accounts and transactions.'''

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, initial_balance = 0):
        if  account_number in self.customers:
            print("Account number already exists")

        else:
            self.customers[account_number] = initial_balance
            print("Account created succesfully") 

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount 
            print("Deposit succesful")

        else:
            print("Account number does not exist")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >=amount:
               self.customers[account_number] -=amount
               print("withdrawal successful")

            else:
                print("insufficient amount")

        else:
            print("Account number does not exist")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")

        else:
            print("Account number does not exist")

bank = Bank()
bank.create_account("SB-123", 1000)
bank.create_account("SB-124", 1500)
bank.make_deposit("SB-123", 500)
bank.make_withdrawal("SB-124", 200)
bank.check_balance("SB-123")
bank.check_balance("SB-124")
                       



             



from datetime import datetime


# 10/14/24

class Bank:
    budget = 0
    customers = list()
    def __init__(self, name, customer):
        self.name = name
        self.customers.append(customer)
        self.budget += customer.balance

    def add_customer(self, customer):
        self.customers.append(customer)
        self.budget += customer.balance

    def remove_customer(self, customer):
        self.customers.remove(customer)
        self.budget -= customer.balance

    def can_get_loan(self, customer, loan):
        if loan / 2 > customer.balance: return False
        return True

class Customer:
    age = 0
    balance = 0
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = datetime.now().year - date_of_birth.year

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

p_1 = Customer("Nika", datetime(2001, 5, 17))
print(p_1.age)
p_1.deposit(1000)
print(p_1.balance)
p_1.withdraw(100)
print(p_1.balance)

b_1 = Bank("Saqartvelos", p_1)
print(b_1.budget)
p_2 = Customer("Irakli", datetime(2003, 6, 19))
p_2.deposit(10000)
b_1.add_customer(p_2)
print(b_1.budget)
b_1.remove_customer(p_1)
print(b_1.budget)
# ====================
# Engage & Apply: Create a Person Class
# ====================

# Creating a Person class with attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name}!"

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

# Creating an instance of Person
person1 = Person("Alice", 25)

# Using the methods
print(person1.greet())            # Output: Hello, my name is Alice!
print(person1.have_birthday())    # Output: Happy Birthday! You are now 26 years old.


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Creating a Student class with attributes and methods
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Method to display a message based on grade
    def display_grade(self):
        return f"{self.name} has a grade of {self.grade}."

    # Method to improve the grade by adding extra points
    def give_extra_credit(self, points):
        self.grade += points
        return f"After extra credit, {self.name}'s grade is now {self.grade}."

# Creating an instance of Student
student1 = Student("John", 85)

# Using the methods
print(student1.display_grade())         # Output: John has a grade of 85.
print(student1.give_extra_credit(5))    # Output: After extra credit, John's grade is now 90.


# ====================
# Final Challenge: Create a BankAccount Class
# ====================

# Creating a BankAccount class with methods for deposit, withdrawal, and balance check
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    # Method to check the balance
    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Creating an instance of BankAccount
account = BankAccount("Alice", 100)

# Testing the methods
print(account.get_balance())    # Output: Current balance: $100.00
print(account.deposit(50))      # Output: Deposited $50.00. New balance: $150.00
print(account.withdraw(30))     # Output: Withdrew $30.00. New balance: $120.00
print(account.withdraw(200))    # Output: Insufficient funds or invalid amount.


# ====================
# My Version of the Final Challenge
# ====================

# Creating a SavingsAccount class with additional methods for interest
class SavingsAccount:
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    # Method to apply interest to the account balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Applied interest. New balance: ${self.balance}"

    # Method to check the balance
    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Creating an instance of SavingsAccount
account2 = SavingsAccount("John", 200)

# Testing the methods
print(account2.get_balance())    # Output: Current balance: $200.00
print(account2.deposit(100))     # Output: Deposited $100.00. New balance: $300.00
print(account2.apply_interest()) # Output: Applied interest. New balance: $315.00
print(account2.withdraw(50))     # Output: Withdrew $50.00. New balance: $265.00

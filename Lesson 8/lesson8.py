# Model a Farm

# In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, 
# keep in mind that there are a number of correct answers.

# The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. 
# This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. 
# Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

#     You should have at least four classes: the parent Animal class, and then at least three child animal classes that inherit from Animal.
#     Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals
#     —such as walking, running, eating, sleeping, and so on.
#     Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.

class Animal:
    def __init__(self, name, age, sound, energy=100):
        self.__name = name
        self.__age = age
        self.__sound = sound
        self.__energy = energy
    
    @property
    def name(self):
        return self.__name  
    @property
    def age(self):
        return self.__age
    @property
    def sound(self):
        return self.__sound
    @property       
    def energy(self):
        return self.__energy    
    
    def eat(self, food):
        self.__energy += food
        print(f"{self.__name} is eating and gaining {food} energy. Total energy: {self.__energy}")

    def sleep(self, hours):
        self.__energy += hours * 2
        print(f"{self.__name} is sleeping for {hours} hours and gaining {hours * 2} energy. Total energy: {self.__energy}")
    
    def speak(self):
        print(f"{self.__name} says: {self.__sound}")   

    def status(self):
        print(f"{self.__name} | Type: {type(self).__name__} | Age: {self.__age} | Energy: {self.__energy}") 

class Cow(Animal):
    def __init__(self, name, age, energy=100, milk_gallons=0):
        super().__init__(name, age, "Moo", energy)
        self.__milk_gallons = milk_gallons

    @property
    def milk_gallons(self):
        return self.__milk_gallons

    def produce_milk(self, gallons):
        if self.energy < 30:
            print(f"{self.name} is too tired to produce milk.")
        else:
            self.__milk_gallons += gallons
            print(f"{self.name} produced {gallons} gallons of milk. Total milk: {self.__milk_gallons} gallons")
    
    def status(self):
        super().status()
        print(f"Milk Gallons: {self.__milk_gallons}")


class Chicken(Animal):
    def __init__(self, name, age, energy=100, egg_count=0):
        super().__init__(name, age, "Cluck", energy)
        self.__egg_count = egg_count

    @property
    def egg_count(self):
        return self.__egg_count

    def lay_egg(self, count):
        self.__egg_count += count
        print(f"{self.name} laid {count} eggs. Total eggs: {self.__egg_count}")
    def status(self):
        super().status()
        print(f"Egg Count: {self.__egg_count}")

class Dog(Animal):
    def __init__(self, name, age, energy=100, breed="Mixed"):
        super().__init__(name, age, "Woof", energy)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed
    
    def herd(self):
        print(f"{self.name} is herding  the other animals. And lost {self.energy * 0.1} energy.")

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {type(animal).__name__} has been added to the farm.")

    def show_animals(self):
        print("Animals on the farm:")
        for animal in self.animals:
            print(f"{animal.name} the {type(animal).__name__}, Age: {animal.age}, Energy: {animal.energy}")
    
    def feed_animals(self, food):
        print(f"Feeding all animals with {food} food.")
        for animal in self.animals:
            animal.eat(food)

    def daily_routine(self):
        for animal in self.animals:
            animal.eat(10)
            animal.sleep(2)
            animal.speak()
            if isinstance(animal, Cow):
                animal.produce_milk(5)
            elif isinstance(animal, Chicken):
                animal.lay_egg(3)
            elif isinstance(animal, Dog):
                animal.herd()

# Example usage:
if __name__ == "__main__":
    farm = Farm()
    cow = Cow("Bessie", 5, 50)
    chicken = Chicken("Clucky", 2, 30)
    dog = Dog("Rover", 3, 40, "Border Collie")

    farm.add_animal(cow)
    farm.add_animal(chicken)
    farm.add_animal(dog)

    farm.daily_routine()
    farm.feed_animals(20)
    farm.show_animals()




# Build a Bank Application
# Objective:

# Develop a command-line banking application that allows users to 
# perform basic banking operations like creating an account, depositing money, and withdrawing money. 
# This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.
# Tasks:
# Step 1: Define the Classes

#    1. Create a class Account with attributes:
#         account_number
#         name
#         balance

#    2. Create a class Bank to manage all accounts. It should have:
#         A dictionary to store accounts (accounts).
#         Methods for each operation:
#             create_account(name, initial_deposit)
#             view_account(account_number)
#             deposit(account_number, amount)
#             withdraw(account_number, amount)
#             save_to_file() and load_from_file() (for file handling).

# Step 2: Implement the Methods

#     Account Creation
#         Generate a unique account_number.
#         Create an Account object and store it in the dictionary.
#         Save account details to a file.

#     View Account Details
#         Prompt the user to input their account number.
#         Retrieve and display the account details if found; otherwise, show an error.

#     Deposit Money
#         Prompt the user for their account number and deposit amount.
#         Validate the amount and update the account balance.

#     Withdraw Money
#         Prompt the user for their account number and withdrawal amount.
#         Validate that the amount is less than or equal to the balance and update the account balance.

#     File Handling
#         Use save_to_file to write account details to accounts.txt.
#         Use load_from_file to load account details when the program starts.

class Account:
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def name(self):
        return self.__name

    @property
    def account_number(self):
        return self.__account_number

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Your account number is {account_number}.")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            print(f"Deposited ${amount:.2f} to account {account_number}. New balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account =  self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                print(f"Withdrew ${amount:.2f} from account {account_number}. New balance: ${account.balance:.2f}")
            else: 
                print("Insufficient funds.")   
        else:            print("Account not found.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.name},{account.balance}\n")
        print("Accounts saved to file successfully.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    account_number, name, balance = line.strip().split(',')
                    self.accounts[int(account_number)] = Account(int(account_number), name, float(balance))
                print("Accounts loaded from file successfully")

        except FileNotFoundError:
            print("File not found. Starting with an empty bank.")   
# Step 2: Implement the Command-Line Interface
#    Create a menu-driven interface that allows users to select operations (create account, view account, deposit, withdraw, save, load) and perform the corresponding actions by calling the methods of the Bank class.
def main():
    bank = Bank("accounts.txt")
    while True:
        print("\nWelcome to the Bank Application!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Save Accounts to File")
        print("6. Load Accounts from File")
        print("7. Exit")

        choice = input("Please select an option (1-7): ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)
        
        elif choice == '2':
            account_number = int(input("Enter account number: "))
            bank.view_account(account_number)

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            bank.save_to_file(bank.filename)

        elif choice == '6':
            bank.load_from_file(bank.filename)

        elif choice == '7':
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
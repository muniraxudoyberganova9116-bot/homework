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

### Boolean Data Type Questions:
#1. Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter your username: ")
password = input("Enter your password: ")   
if username!=" " and password!="":
    print("Username and password are valid.")
else:
    print("Username and password cannot be empty.")

#2. Create a program that checks if two numbers are equal and outputs a message if they are.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
    print("The two numbers are equal.")
else:
    print("The two numbers are not equal.")

#3. Write a program that checks if a number is positive and even.
number = int(input("Enter a number: "))
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")   
#4. Write a program that takes three numbers and checks if all of them are different.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All three numbers are different.")
else:
    print("Not all three numbers are different.")       
#5. Create a program that accepts two strings and checks if they have the same length.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) == len(string2):
    print("The two strings have the same length.")
else:
    print("The two strings do not have the same length.")   
#6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:     
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")   
#7. Write a program that checks if the sum of two numbers is greater than 50.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 + num2 > 50:
    print("The sum of the two numbers is greater than 50.")
else:    
    print("The sum of the two numbers is not greater than 50.")

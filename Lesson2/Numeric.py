### Number Data Type Questions:

#1. Create a program that takes a float number as input and rounds it to 2 decimal places.

a =float(input("Enter a float number: "))
rounded_a = round(a, 2)
print("Rounded number to 2 decimal places:", rounded_a)

#2. Write a Python file that asks for three numbers and outputs the largest and smallest.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: ")) 
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("The largest number is:", largest)
print("The smallest number is:", smallest)

#3. Create a program that converts kilometers to meters and centimeters.
km = float(input("Enter the distance in kilometers: "))
m = km * 1000
cm = km * 100000
print("Distance in meters:", m)
print("Distance in centimeters:", cm)

#4. Write a program that takes two numbers and prints out the result of integer division and the remainder.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
div = num1 // num2
rem = num1 % num2
print("Result of integer division:", div)
print("Remainder:", rem)

#5. Make a program that converts a given Celsius temperature to Fahrenheit.
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#6. Create a program that accepts a number and returns the last digit of that number.
num = int(input("Enter a number: "))
last_digit = num % 10
print("The last digit of the number is:", last_digit)

#7. Create a program that takes a number and checks if it’s even or not.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 


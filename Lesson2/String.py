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



### String Questions:

#1. Create a program to ask name and year of birth from user and tell them their age.

name = input("Please enter your name: ")
year_of_birth = int(input("Please enter your year of birth: "))
current_year = 2026
age = current_year - year_of_birth
print(f"Hello {name}, you are {age} years old.")

#2. Extract car names from this text:
txt = 'LMaasleitbtui'
car_names = ['L', 'M', 'a', 's', 'l', 'e', 'i', 't', 'b', 'u', 'i']
extracted_car_names = ''.join(car_names)
print("Extracted car names:", extracted_car_names)      

#3. Write a Python program to:
'''   - Take a string input from the user.
   - Print the length of the string.
   - Convert the string to uppercase and lowercase.'''
user_string = input("Please enter a string: ") 
string_length = len(user_string)
uppercase_string = user_string.upper()
lowercase_string = user_string.lower()
print(f"Length of the string: {string_length}")
print(f"String in uppercase: {uppercase_string}")
print(f"String in lowercase: {lowercase_string}")


#4. Write a Python program to check if a given string is `palindrome` or not.
#> What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
  
word = input("Enter a string to check if it's a palindrome: ")
word=word.replace(" ", "").lower()  # Remove spaces and convert to lowercase
word_reversed = word[::-1]  # Reverse the string
if word == word_reversed:
    print("The string is a palindrome.")
else:    
    print("The string is not a palindrome.")   

#  5. Write a program that counts the number of vowels and consonants in a given string.
input_string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = 0
consonant_count = 0
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")   


#6. Write a Python program to check if one string contains another.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string2 in string1:
    print(f'"{string1}" contains "{string2}".')
else:
    print(f'"{string1}" does not contain "{string2}".')


#7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
'''Example:  
   - Input sentence: "I love apples."  
   - Replace: "apples"  
   - With: "oranges"  
   - Output: "I love oranges."'''

sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word you want to replace: ")
replacement_word = input("Enter the word you want to use as a replacement: ")
new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", new_sentence)


#8. Write a program that asks the user for a string and prints the first and last characters of the string.  
user_input = input("Enter a string: ")
if len(user_input) > 0:
    first_character = user_input[0]
    last_character = user_input[-1]
    print(f"First character: {first_character}")
    print(f"Last character: {last_character}")
else:
    print("You entered an empty string.")

#9. Ask the user for a string and print the reversed version of it.
user_string = input("Enter a string to reverse: ")
reversed_string = user_string[::-1]
print("Reversed string:", reversed_string)  

#10. Write a program that asks the user for a sentence and prints the number of words in it.  
sentence = input("Enter a sentence: ")
words = sentence.split()  # Split the sentence into words
word_count = len(words)  # Count the number of words
print(f"Number of words in the sentence: {word_count}")     

#11. Write a program to check if a string contains any digits.  
user_string = input("Enter a string: ")
contains_digits = any(char.isdigit() for char in user_string)
if contains_digits:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")    

#12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
words_list = input("Enter a list of words separated by spaces: ").split()
separator = input("Enter the separator character: ")
result = separator.join(words_list)
print("Joined string:", result)

#13. Ask the user for a string and remove all spaces from it.  
user_string = input("Enter a string: ")
string_without_spaces = user_string.replace(" ", "")
print("String without spaces:", string_without_spaces)

#14. Write a program to ask for two strings and check if they are equal or not.  
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

#  15. Ask the user for a sentence and create an acronym from the first letters of each word.  
   #Example:  
    #- Input: "World Health Organization"  
    #- Output: "WHO"   '''
sentence = input("Enter a sentence: ")
words = sentence.split()  # Split the sentence into words
acronym = ''.join(word[0].upper() for word in words if word)  # Take the first letter of each word and convert to uppercase
print("Acronym:", acronym)  

#16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
user_string = input("Enter a string: ")
character_to_remove = input("Enter the character to remove: ")
updated_string = user_string.replace(character_to_remove, "")
print("String after removing the character:", updated_string)   

#17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
user_string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for vowel in vowels:
    user_string = user_string.replace(vowel, '*')
print("String after replacing vowels with '*':", user_string)
#18. Write a program that checks if a string starts with one word and ends with another.  
    #Example:  
    #- Input: "Python is fun!"  
    #- Starts with: "Python"  
    #- Ends with: "fun!"  """"
user_string = input("Enter a string: ")
start_word = input("Enter the word that the string should start with: ")
end_word = input("Enter the word that the string should end with: ")
if user_string.startswith(start_word) and user_string.endswith(end_word):
    print("The string starts with the specified word and ends with the specified word.")
else:    
    print("The string does not start with the specified word and/or does not end with the specified word.")    


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

# ## Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>

# 2.  What is the difference between the continue and break statements in Python?
#     - The `continue` statement is used to skip the current iteration of a loop and move to the next iteration. 
#      When `continue` is encountered, the rest of the code inside the loop for that iteration is ignored, and the loop proceeds with the next iteration.
#     - The `break` statement is used to exit the loop entirely. 
#      When `break` is encountered, the loop is terminated immediately, and the program continues with the code that follows the loop.

# 3. Can you explain the difference between for loop and while loop?
#     - A `for` loop is used to iterate over a sequence (like a list, tuple, string, or range) and executes a block of code for each item in the sequence. 
#      It is generally used when the number of iterations is known beforehand.
#     - A `while` loop is used to execute a block of code as long as a specified condition is true. 
#      It is generally used when the number of iterations is not known and the loop needs to continue until a certain condition is met.

# 4. How would you implement a nested for loop system? Provide an example.
#     A nested for loop is a loop inside another loop. The inner loop will be executed for each iteration of the outer loop.
#     Example:
#     ```python
#     for i in range(1, 4):  # Outer loop
#         for j in range(1, 4):  # Inner loop
#             print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")
#     ```
#     Output:
#     ```
#     Outer loop iteration: 1, Inner loop iteration: 1
#     Outer loop iteration: 1, Inner loop iteration: 2
#     Outer loop iteration: 1, Inner loop iteration: 3
#     Outer loop iteration: 2, Inner loop iteration: 1
#     Outer loop iteration: 2, Inner loop iteration: 2
#     Outer loop iteration: 2, Inner loop iteration: 3
#     Outer loop iteration: 3, Inner loop iteration: 1
#     Outer loop iteration: 3, Inner loop iteration: 2
#     Outer loop iteration: 3, Inner loop iteration: 3  

# ## Homeworks:

# **1.** Return uncommon elements of lists. Order of elements does not matter.
print("task1")
# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]

# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]

# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]

test_cases = [
    ([1, 1, 2], [2, 3, 4]),
    ([1, 2, 3], [4, 5, 6]),
    ([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]),
]

for list1, list2 in test_cases:
    right = list2[:]
    uncommon = []

    for item in list1:
        found = False
        index = 0
        while index < len(right):
            if item == right[index]:
                right.pop(index)
                found = True
                break
            index += 1
        if not found:
            uncommon.append(item)

    for item in right:
        uncommon.append(item)

    print(uncommon)


# **2.** Print the square of each number which is less than `n` on a separate line.
print("\ntask2")
#n = input("Enter a number: ")
#n = int(n)
n = 5
for i in range(n):
    if i+1 == n:
        break
    i = i+1
    print(i ** 2)

# **3.** 'txt' is a string variable. 

#after every third character in `txt`, an underscore should be added.
# if the character is a vowel or if it is followed by an underscore, an underscore should be added after the next character.
#  if the character is the last character in the string, no underscore should be added.

# input: hello # output: hel_lo
# input: assalom # output: ass_alom
# input: abcabcdabcdeabcdefabcdefg # output: abc_abcd_abcdeab_cdef_abcdefg
print("\ntask3")
txt = input("Enter the text:  ")
txt = list(txt)
vowels = "aeiou"
output = []
for l in range(len(txt)):
    output.append(txt[l])
    if (l + 1) % 3 == 0 and l != len(txt) - 1:
        output.append("_")
        while txt[l] in vowels and l < len(txt) - 1 and txt[l+1] == "_":
            output.insert(l+2, "_")
txt = "".join(output)
print(txt)

# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

# > Hint: Use Python’s `random.randint()` to generate the number.
print("\ntask4")
import random   
number_to_guess = random.randint(1, 100)
attempts = 10
while attempts > 0:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess > number_to_guess:
        print("Too high!")
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    attempts -= 1
else:
    print("You lost. Want to play again? ")
    play_again = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ")
    if play_again in ['Y', 'YES', 'y', 'yes', 'ok']:
        number_to_guess = random.randint(1, 100)
        attempts = 10
        while attempts > 0:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess > number_to_guess:
                print("Too high!")
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("You guessed it right!")
                break
            attempts -= 1   


# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."
print("\ntask5")
password = input("Enter a password: ")
if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")    

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

# ---
print("\ntask6")
for num in range(2, 101):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)  

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# First to 5 points wins the match.

print("\ntask bonus")
import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0  
while player_score < 5 and computer_score < 5:
    computer_choice = random.choice(choices)
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):      
        print(f"You chose {player_choice}. Computer chose {computer_choice}. You win!")
        player_score += 1
    else:
        print(f"You chose {player_choice}. Computer chose {computer_choice}. Computer wins!")
        computer_score += 1

print(f"Final score - You: {player_score}, Computer: {computer_score}")
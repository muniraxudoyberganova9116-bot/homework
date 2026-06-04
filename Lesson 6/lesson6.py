### Zero Check Decorator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        else:
            return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b    

print(div(6, 2))
print(div(6, 0))

# ### **Employee Records Manager**

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Emplyee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!")

#menu
while True:
    print("\nEmployee Records Manager")
    print("\n1. Add new employee record")
    print("\n2. View all employee records")
    print("\n3. Search for an employee by Employee ID")
    print("\n4. Update an employee's information")
    print("\n5. Delete an employee record")
    print("\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        with open("employees.txt", "r") as file:
            records = file.readlines()
            for record in records:
                print(record.strip())
    elif choice == '3':
        emp_id = input("Enter Employee ID to search:")
        with open("employees.txt", "r") as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id):
                    print(record.strip())
                    break
            else:
                print("Employee not found.")
    elif choice == '4':
        emp_id = input("Enter Employee ID to update:")
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                else:
                    file.write(record)
        print("Employee updated successfully!")
    elif choice == '5':
        emp_id = input("Enter Employee ID to delete:")  
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if not record.startswith(emp_id):
                    file.write(record)
        print("Employee deleted successfully!")
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  


# ### **Word Frequency Counter**
with open("sample.txt", "r") as file:
    text = file.read()
    if not text:
        text = input("sample.txt is empty. Please enter a paragraph to create the file: ")
        with open("sample.txt", "w") as file:
            file.write(text)
import string
def count_word_frequency(text):
    word_count = {}
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
word_count = count_word_frequency(text)
total_words = sum(word_count.values())
print(f"Total number of words: {total_words}")
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
top_5_words = sorted_word_count[:5]
print("Top 5 most common words:")
for word, count in top_5_words:
    print(f"{word}: {count}")
with open("word_count_report.txt", "w") as file:
    file.write(f"Total number of words: {total_words}\n")
    file.write("Top 5 most common words:\n")
    for word, count in top_5_words:
        file.write(f"{word}:{count}\n")

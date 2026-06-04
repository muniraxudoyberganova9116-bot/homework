# ### **Employee Records Manager**
# **Objective**: Create a program to manage employee records using file handling.  

# **Tasks**:  
# 1. **File Creation and Data Entry**  
#    - Create a file named **"employees.txt"**.  
#    - Allow the user to add new employee records. Each record should have the following fields:  
     
#      Employee ID, Name, Position, Salary
     
#      Example of a record:  
     
#      1001, John Doe, Software Engineer, 75000
     
# 2. **Menu Options**  
#    Your program should present the following options:  
   
#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit
   
# 3. **Functional Requirements**  
#    - **Option 1**: Append a new employee record to **"employees.txt"**.  
#    - **Option 2**: Display all employee records from **"employees.txt"**.  
#    - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program. 
# ---

# Employee Records Manager

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

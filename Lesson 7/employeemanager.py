# Employee Records Manager (OOP Version)

# Objective: Create a program to manage employee records using classes and file handling.
# file name as variable 
f = "employees.txt"

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
    def save_to_file(self):
        with open(f, 'a') as file:
            file.write(f"{self.emp_id},{self.name},{self.position},{self.salary}\n")
        

    
class EmployeeManager:
    def add_employee(self, emp_id, name, position, salary):
        employee = Employee(emp_id, name, position, salary)
        employee.save_to_file()
        print("Employee added successfully!")

    def view_employees(self):
        with open(f, 'r') as file:
            records = file.readlines()
            for record in records:
                print(record.strip())

    def search_employee(self, emp_id):
        with open(f, 'r') as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id):
                    print(record.strip())
                    break
            else:
                print("Employee not found.")
    

    def update_employee(self, emp_id, name, position, salary):
        with open(f, 'r') as file:
            records = file.readlines()
        with open(f, 'w') as file:
            for record in records:
                if record.startswith(emp_id):
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    print("Employee updated successfully!")
                else:
                    print("Employee not found. Adding new employee.")
                    self.add_employee(emp_id, name, position, salary)
                    file.write(record)
        save_to_file()
        

    def delete_employee(self, emp_id):
        with open(f, 'r') as file:
            records = file.readlines()
        with open(f, 'w') as file:
            for record in records:
                if not record.startswith(emp_id):
                    file.write(record)
        print("Employee deleted successfully!")
        
    
    def menu(self):
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
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                salary = input("Enter Employee Salary: ")
                self.add_employee(emp_id, name, position, salary)
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                emp_id = input("Enter Employee ID to search:")
                self.search_employee(emp_id)
            elif choice == '4':
                emp_id = input("Enter Employee ID to update:")
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                self.update_employee(emp_id, name, position, salary)
            elif choice == '5':
                emp_id = input("Enter Employee ID to delete:")  
                self.delete_employee(emp_id)
            elif choice == '6':
                print("Exiting the program. Goodbye!")
                
                break
            else:
                print("Invalid choice. Please try again.")

manager = EmployeeManager()
manager.menu()
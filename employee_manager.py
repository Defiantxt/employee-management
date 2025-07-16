"""
Employee Management System (CLI)
Author: Phillip
Description:
A simple command-line program that allows users to:
- Add new employees
- Search for employees
- Update employee data
- View all employees
All data is stored in a CSV file.
"""
import csv

def main_menu():
    """Displays the main menu and returns the user's choice."""
    while True:
        print("1. Add New Employees")
        print("2. Search Employees")
        print("3. Update Employee Data")
        print("4. View All Employees")
        print('Press "q" to Quit')
        user_input = input(">").lower().strip()

        valid_input = ["1", "2", "3", "4", "q"]
        if user_input in valid_input:
            return user_input
        else:
            print("Enter valid Input❌\n")
            continue


def add_employee():
    """Prompts user for employee info and appends it to the CSV file."""
    with open('employee_file.csv', mode='a', newline='') as csv_file:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        emp_name = input("Enter Employee name: ").lower().capitalize()
        dept = input("Enter Department: ").lower().capitalize()
        birth_month = input("Enter Birth month: ").lower().capitalize()
        if csv_file.tell() == 0:
            writer.writeheader()
            print("Headers Added!")
            writer.writerow({'emp_name': emp_name, 'dept': dept, 'birth_month': birth_month})
            print("Employee Added!")
        else:
            writer.writerow({'emp_name': emp_name, 'dept': dept, 'birth_month': birth_month})
            print("Employee Added!")


def search_employee():
    """Searches for an employee by name and displays matching results."""
    with open("employee_file.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        employee_name = input("Enter Employee name: ").lower().capitalize()
        found = False
        for row in csv_reader:
            if employee_name in row['emp_name']:
                print("Match found✅")
                print(f"Employee name: {row['emp_name'].capitalize()} | Department: {row['dept'].capitalize()} | Birth month: {row['birth_month'].capitalize()}\n")
                found = True
        if not found:
            print("No matches found❌")
            return


def update_employee():
    """Finds an employee and lets the user update their info."""
    with open("employee_file.csv", mode="r", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        employees = list(csv_reader)

    employee_name = input("Enter Employee name: ").lower()
    found = False

    for row in employees:
        if employee_name in row['emp_name'].lower():
            print("Match found ✅")
            found = True

            def ask_yes_or_no(question):
                while True:
                    answer = input(question + "y/n: ").strip().lower()
                    if answer == "y":
                        return True
                    elif answer == "n":
                        return False
                    else:
                        print("Please answer with 'y' or 'n'.")

            if ask_yes_or_no("Do you want to update Name? "):
                row['emp_name'] = input("Enter new Name: ")

            if ask_yes_or_no("Do you want to update Department? "):
                row['dept'] = input("Enter new Department: ")

            if ask_yes_or_no("Do you want to update Birth Month? "):
                row['birth_month'] = input("Enter new Birth Month: ")

    if found:
        with open("employee_file.csv", mode="w", newline='') as csv_file:
            fieldnames = ['emp_name', 'dept', 'birth_month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
        print("✅ Data updated successfully.")
    else:
        print("❌ No match found.")
        return


def view_employees():
    """Displays all employees currently stored in the CSV file."""
    with open("employee_file.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(f"Employee name: {row['emp_name'].capitalize()} | Department: {row['dept'].capitalize()} | Birth month: {row['birth_month'].capitalize()}")


def confirm_quit():
    """Asks user for confirmation before quitting. Returns True if confirmed."""
    confirm = input("Are you sure you want to quit? (y/n): ").lower()
    return confirm == "y"


while True:
    main = main_menu()
    if main == "1":
        add_employee()
    elif main == "2":
        search_employee()
    elif main == "3":
        update_employee()
    elif main == "4":
        view_employees()
    elif main == "q":
        if confirm_quit():
            break


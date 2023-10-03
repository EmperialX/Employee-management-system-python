import os
import json

class Employee:
    def __init__(self, employ_id, name, father_name, email, department, employ_contact, employ_salary):
        self.employ_id = employ_id
        self.name = name
        self.father_name = father_name
        self.email = email
        self.department = department
        self.employ_contact = employ_contact
        self.employ_salary = employ_salary

class MainMenu:
    def menu(self):
        print("\t********************************************")
        print("\t*                                          *")
        print("\t*     ********************************     *")
        print("\t*     *  EMPLOYEE MANAGEMENT SYSTEM  *     *")
        print("\t*     ********************************     *")
        print("\t*                                          *")
        print("\t*            [Welcome to EMS]              *")
        print("\t*                                          *")
        print("\t********************************************")
        print("\n\nPress 1 : To Add an Employee Details")
        print("Press 2 : To See an Employee Details ")
        print("Press 3 : To Remove an Employee")
        print("Press 4 : To Update Employee Details")
        print("Press 5 : To Calculate Total Monthly Payroll")
        print("Press 6 : To Find Employees in a Specific Department")
        print("Press 7 : To Find Employees with Highest and Lowest Salaries")
        print("Press 8 : To Give Salary Raise to All Employees")
        print("Press 9 : To Exit the EMS Portal")

class Employee_Add:
    def __init__(self):
        self.loadEmployeesFromFiles()

    def loadEmployeesFromFiles(self):
        self.employees = []
        for filename in os.listdir("."):
            if filename.startswith("emp") and filename.endswith(".json"):
                with open(filename, "r") as file:
                    employee_data = json.load(file)
                    self.employees.append(employee_data)

    def createEmployee(self, employ_id, name, father_name, email, department, employ_contact, employ_salary):
        employee_data = {
            "employ_id": employ_id,
            "name": name,
            "father_name": father_name,
            "email": email,
            "department": department,
            "employ_contact": employ_contact,
            "employ_salary": employ_salary
        }

        self.employees.append(employee_data)
        emp_id = self.saveEmployeeToFile(employ_id)
        return emp_id  # Return the employee ID

    def saveEmployeeToFile(self, employ_id):
        filename = f"{employ_id}.json"
        with open(filename, "w") as file:
            json.dump(self.employees[-1], file, indent=4)
        return employ_id  # Return the employee ID

    def createFile(self, emp_id):
        print("Enter Employee's details:")
        name = input("Enter Employee's name --------: ")
        father_name = input("Enter Employee's Father name -: ")
        email = input("Enter Employee's Email ID ----: ")
        department = input("Enter Employee's department ----: ")
        employ_contact = input("Enter Employee contact Info --: ")
        employ_salary = input("Enter Employee's Salary ------: ")

        emp_id = self.createEmployee(emp_id, name, father_name, email, department, employ_contact, employ_salary)

        print(f"\nEmployee has been Added with ID: {emp_id}\n")
        input("\nPress Enter to Continue...")

class Employee_Show:
    def viewFile(self, employ_id):
        filename = f"{employ_id}.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                employee_data = json.load(file)
                print(f"Employee ID: {employee_data['employ_id']}")
                print(f"Employee Name: {employee_data['name']}")
                print(f"Father's Name: {employee_data['father_name']}")
                print(f"Employee Contact: {employee_data['employ_contact']}")
                print(f"Email Information: {employee_data['email']}")
                print(f"Employee department: {employee_data['department']}")
                print(f"Employee Salary: {employee_data['employ_salary']}")
        else:
            print("\nEmployee not found :(")

class Employee_Remove:
    def removeEmployee(self, employ_id):
        filename = f"{employ_id}.json"
        if os.path.exists(filename):
            os.remove(filename)  # Remove the associated file
            print("\nEmployee has been removed Successfully")
        else:
            print("\nEmployee does not exist :( ")

class Employee_Update:
    def updateEmployee(self, employ_id, attribute, new_value):
        filename = f"{employ_id}.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                employee_data = json.load(file)
                employee_data[attribute] = new_value
            with open(filename, "w") as file:
                json.dump(employee_data, file, indent=4)
            print(f"\n{attribute} has been updated Successfully")
        else:
            print("\nEmployee not found :(")

class Employee_Calculator:
    def calculateTotalMonthlyPayroll(self):
        total_salary = sum(float(employee["employ_salary"]) for employee in Employee_Add().employees)
        print(f"\nTotal Monthly Payroll: {total_salary}")

    def findEmployeesInDepartment(self, department):
        employees_in_department = [employee for employee in Employee_Add().employees if employee["department"] == department]
        if employees_in_department:
            print("\nEmployees in Department:")
            for employee in employees_in_department:
                print(f"Employee ID: {employee['employ_id']}, Name: {employee['name']}")
        else:
            print("\nNo employees in the specified department.")

    def findEmployeesWithHighestAndLowestSalaries(self):
        if not Employee_Add().employees:
            print("\nNo employees found.")
            return

        employees_sorted_by_salary = sorted(Employee_Add().employees, key=lambda x: float(x["employ_salary"]))
        lowest_salary_employee = employees_sorted_by_salary[0]
        highest_salary_employee = employees_sorted_by_salary[-1]

        print("\nEmployee with the Lowest Salary:")
        print(f"Employee ID: {lowest_salary_employee['employ_id']}, Name: {lowest_salary_employee['name']}")
        print(f"Lowest Salary: {lowest_salary_employee['employ_salary']}")

        print("\nEmployee with the Highest Salary:")
        print(f"Employee ID: {highest_salary_employee['employ_id']}, Name: {highest_salary_employee['name']}")
        print(f"Highest Salary: {highest_salary_employee['employ_salary']}")

class Employee_Raise:
    def raiseSalary(self, percentage):
        for employee in Employee_Add().employees:
            new_salary = float(employee["employ_salary"]) * (1 + percentage / 100)
            employee["employ_salary"] = str(new_salary)
        Employee_Add().saveEmployeeToFile()
        print("\nSalaries have been raised by {}%".format(percentage))

class CodeExit:
    def out(self):
        print("\n*****************************************")
        print("$ cat Thank You For Using my Software :) ")
        print("*****************************************")
        exit(0)

class EmployManagementSystem:
    def main(self):
        os.system("cls" if os.name == "nt" else "clear")
        i = 0
        obj1 = MainMenu()
        obj1.menu()
        while i < 10:
            print("\nPlease Enter choice :", end=" ")
            i = int(input())
            if i == 1:
                emp_id = f"emp{len(Employee_Add().employees) + 1}"
                ep = Employee_Add()
                ep.createFile(emp_id)
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 2:
                print("Please Enter Employee's ID (e.g., emp3):", end=" ")
                employ_id = input()
                Employee_Show().viewFile(employ_id)
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 3:
                print("Please Enter Employee's ID (e.g., emp3):", end=" ")
                employ_id = input()
                Employee_Remove().removeEmployee(employ_id)
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 4:
                print("Please Enter Employee's ID (e.g., emp3):", end=" ")
                employ_id = input()
                print("Please Enter the detail you want to Update (name, father_name, email, department, employ_contact, employ_salary):", end=" ")
                attribute = input()
                print(f"Please Enter the Updated {attribute}:", end=" ")
                new_value = input()
                Employee_Update().updateEmployee(employ_id, attribute, new_value)
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 5:
                Employee_Calculator().calculateTotalMonthlyPayroll()
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 6:
                print("Please Enter the Department Name:", end=" ")
                department = input()
                Employee_Calculator().findEmployeesInDepartment(department)
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 7:
                Employee_Calculator().findEmployeesWithHighestAndLowestSalaries()
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 8:
                print("Enter the percentage raise for salaries:", end=" ")
                percentage = float(input())
                Employee_Raise().raiseSalary(percentage)
                input("\nPress Enter to Continue...")
                os.system("cls" if os.name == "nt" else "clear")
                obj1.menu()
            elif i == 9:
                obj = CodeExit()
                obj.out()

if __name__ == "__main__":
    EMS = EmployManagementSystem()
    EMS.main()

import sys
import gc

class Company:
    def __init__(self, cname):
        self.cname = cname
        self.employees = []   # empty list

    class Employee:
        def __init__(self, emp_id, emp_name, company):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.company = company   # reference to Company

        def display_details(self):
            print(f"Employee ID: {self.emp_id}, Name: {self.emp_name}, Company: {self.company.cname}")

    def add_employee(self, emp_id, emp_name):
        emp = Company.Employee(emp_id, emp_name, self)
        self.employees.append(emp)

        print(f"\nEmployee {emp_name} hired.")
        print("Employee reference count:", sys.getrefcount(emp))
        print("Company reference count:", sys.getrefcount(self))

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"\nRemoving Employee {emp.emp_name}")
                print("Reference count before deletion:", sys.getrefcount(emp))

                self.employees.remove(emp)
                del emp

                gc.collect()
                print("Garbage collection done.")
                return

        print("Employee not found")
    def display_all(self):
        if not self.employees:
            print("No employees in the company.")
        else:
            print(f"\nEmployees in {self.cname}:")
            for emp in self.employees:
                emp.display_details()

print("\n\tDISPLAYING EMPLOYEE DETAILS....\n")
cname = input("Enter Company Name: ")
company = Company(cname)

num_employees = int(input("Enter number of employees: "))

for i in range(num_employees):
    print(f"\nEnter details of employee {i+1}...\n")
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    company.add_employee(emp_id, emp_name)

print("\n--- Employee Details Before Removal ---")
company.display_all()

remove_count = int(input("\nEnter number of employees to remove: "))

for i in range(remove_count):
    emp_id = int(input("Enter Employee ID to remove: "))
    company.remove_employee(emp_id)

print("\n--- Employee Details After Removal ---")
company.display_all()

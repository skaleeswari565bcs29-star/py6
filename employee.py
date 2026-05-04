import gc
class Employee:
    class Address:
        def __init__(self, city, state, pin):
            self.city = city
            self.state = state
            self.pc = pin
        def display(self):
            print("City:", self.city, "State:", self.state, "Pincode:", self.pc)

    def __init__(self, id, name, city, state, pin):
        self.id = id
        self.name = name
        self.add = Employee.Address(city, state, pin)

    def display_EMP(self):
        print("\nEmployee Details..")
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Address:")
        self.add.display()
n = int(input("Enter no of employees: "))
emp = []
print("\n---Hiring Process---")
for i in range(n):
    print("\nDetails of Employee", i + 1)
    emp_id = int(input("Enter id: "))
    name = input("Enter name: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    pin = input("Enter pincode: ")
    emp.append(Employee(emp_id, name, city, state, pin))
for e in emp:
    e.display_EMP()
print("\n---Resignation Process---")
d = int(input("Employee ID to be deleted: "))
f = 0
for e in emp:
    if e.id == d:
        print("Removing employee", e.name)
        emp.remove(e)
        f = 1
        break
if not f:
    print("Employee not found")
gc.collect()
print("\n---Remaining Employee---")
for e in emp:
    e.display_EMP()
print("\ndeleting all employees")
emp.clear()
gc.collect()

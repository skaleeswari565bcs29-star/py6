import sys
import gc

class University:
    def __init__(self,university_name):
        self.uni=university_name
        self.students=[]
    class Student:
        def __init__(self,university,rno,n):
            self.roll=rno
            self.univ=university
            self.name=n
        def display_details(self):
            print("Roll No:",self.roll,"Name:",self.name,"University Name:",self.univ)
    def add_stu(self, rno, n):
        # Accessing inner class via self.Student
        student=self.Student(self.uni, rno, n)
        self.students.append(student)
        print("Reference count of student:",sys.getrefcount(student))
        print("Reference Count of University:",sys.getrefcount(self))
        return self.students

    def remove_stu(self,roll):
        for student in self.students:
            if student.roll==roll:
                print("Removing Student:",student.name)
                self.students.remove(student)
                return 1
        print("Student not Found..")
        return None

    def display(self):
        print("\nAll Students:")
        for student in self.students:
            student.display_details()
uname=input("Enter University Name:")
u=University(uname)
n=int(input("Enter no of Students:"))
for i in range(n):
    print("\nEnter details of student",i+1)
    roll=int(input("Enter Roll No:"))
    name=input("Enter Name:")
    u.add_stu(roll,name)
u.display()
r=int(input("Enter the roll no to be deleted:"))
u.remove_stu(r)
u.display()
gc.collect()

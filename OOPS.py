
from abc import ABC, abstractmethod

print('===== STUDENT MANAGEMENT SYSTEM =====')

students = []

# Abstraction
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_type(self):
        pass


# Inheritance
class Student(Person):
    def __init__(self, name, roll_number, marks):
        super().__init__(name)
        self.roll_number = roll_number
        self.__marks = marks

    # Encapsulation
    def Display(self):
        print("Student name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.__marks)
        print("Student Type:", self.display_type())

    def view_marks(self):
        return self.__marks

    def update_marks(self, new):
        if 0 <= new <= 100:
            self.__marks = new
            print("Marks updated successfully!")
        else:
            print("Marks must be between 0 and 100.")

    def check_results(self):
        if self.__marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Polymorphism
class RegularStudent(Student):
    def display_type(self):
        return 'Regular Student'


class OnlineStudent(Student):
    def display_type(self):
        return 'Online Student'


# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. View Marks")
    print("4. Update Marks")
    print("5. Check Result")
    print("6. Exit")

    try:
        n = int(input("Enter your choice: "))

        if n == 1:
            name = input("Enter student name: ")
            roll_number = int(input("Enter roll number: "))
            marks = float(input("Enter marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue

            print("1. Regular Student")
            print("2. Online Student")
            student_type = int(input("Choose student type: "))

            if student_type == 1:
                s = RegularStudent(name, roll_number, marks)
            elif student_type == 2:
                s = OnlineStudent(name, roll_number, marks)
            else:
                print("Invalid student type!")
                continue

            students.append(s)
            print("Student added successfully!")

        elif n == 2:
            if len(students) == 0:
                print("No students found!")
            else:
                for s in students:
                    print("\n----------------")
                    s.Display()

        elif n == 3:
            r = int(input("Enter roll number: "))
            found = False

            for s in students:
                if s.roll_number == r:
                    print("Current marks:", s.view_marks())
                    found = True
                    break

            if not found:
                print("Roll number not found!")

        elif n == 4:
            r = int(input("Enter roll number: "))
            found = False

            for s in students:
                if s.roll_number == r:
                    new_marks = float(input("Enter new marks: "))
                    s.update_marks(new_marks)
                    found = True
                    break

            if not found:
                print("Roll number not found!")

        elif n == 5:
            r = int(input("Enter roll number: "))
            found = False

            for s in students:
                if s.roll_number == r:
                    s.check_results()
                    found = True
                    break

            if not found:
                print("Roll number not found!")

        elif n == 6:
            print("Thank you for using Student Management System!")
            break

        else:
            print("Enter a valid choice!")

    except ValueError:
        print("Please enter valid numeric input!")

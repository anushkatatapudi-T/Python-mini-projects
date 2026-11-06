class Person:
    def display(self):
        print("I am a person")
class Student(Person):
    def display(self):
        super().display()
        print("Iam a student")
p = Student()
p.display()
class Employee:
    def company(self):
        print("I'm working in a company")
class developer(Employee):
    def dev(self):
        print("Working as a developer")
class designer(Employee):
    def design(self):
        print("Working as designer")

c1 = designer()
c2 = developer()
c1.company()
c2.company()
c1.design()
c2.dev()
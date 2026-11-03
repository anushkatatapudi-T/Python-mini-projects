def calculate_expense(food,travel):
    return food + travel
result = calculate_expense(209,700)
print(result)
def add_expense(amount, tax=0):
    return amount + tax

print(add_expense(100))
print(add_expense(100, 10))
def calculate_expense(category,amount):
    return category +" "+ str(amount)

print(calculate_expense(amount = 333 , category ='food'))
def exp(*args):
    return sum(args)
print(exp(200,200))
print(exp(200,200,300,300))
def exp(**kwargs):
    return sum(kwargs.values())
print(exp(food=300,travel=200,juice=100))

def cal(category,*amount,discount=0):
    return sum(amount) - discount
print(cal("Food", 200, 300, 100, discount=50))

expenses = [150, 250, 100, 500]
print(expenses[0])
print(expenses[-1])
print(sum(expenses))
expenses.append(100)
print(expenses)

exp = {
    "Category": "Travel",
    "amount": 180,
    "Payment method": "UPI"
}
print(exp['Category'])
print(exp['amount'])
exp['amount'] = 250
print(exp['amount'])
exp['date'] ="2026-10-29"
print(exp)

expenses = [
    {"category": "Food", "amount": 200},
    {"category": "Travel", "amount": 150},
    {"category": "Shopping", "amount": 500}
]
print(expenses[2]['category'])
print(expenses[0]['amount'])
print(expenses[0]['amount']+expenses[1]['amount']+expenses[2]['amount'])

exp=[200,300,350]
total=0
for amount in exp :
    total = total + amount
print(total)

expenses = [
    {"category": "Food", "amount": 200},
    {"category": "Travel", "amount": 150},
    {"category": "Shopping", "amount": 500}
]
total= 0
for word in expenses:
    total = total + word['amount']

print(total)

expenses = [
    {"category": "Food", "amount": 200},
    {"category": "Travel", "amount": 150},
    {"category": "Food", "amount": 100},
    {"category": "Shopping", "amount": 500}
]
total = 0
for expense in expenses :
    if expense['category'] == "Food":
        total = total + expense['amount']
print(total)

with open('my_expenses.txt','w') as file :
    file.write('food:300\n')
    file.write('travel:150\n')
with open('my_expenses.txt','r') as file :
    content = file.read()
print(content)

import json
expenses = [
    {'category':'food','amount':300},
    {'category':'Shopping','amount':3000},
    {'category':'Travel','amount':1200}

]
with open('expense.json','w') as file :
    json.dump(expenses,file,indent = 4)

import json
expense=[
    {'Food':250},
    {'Shopping':400}
]
result=[]
with open('exp.json','w') as file :
    json.dump(expense,file,indent=4)
    result.append(expense)
with open('exp.json','r') as file :
    json.load(file)
    result = json.load(file)
print(result)    

#class and objects
class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print('Student : ' , self.name)
        print('Marks : ',self.marks)
        
    def is_pass(self):
        if  self.marks >= 40 :
            return self.name + " " + 'passed!'
        else :
            return self.name + " " + 'failed!'
    def update_marks(self,new_marks):
        self.marks = new_marks
        return self.marks
s1=Student('Anushka',90)
s2=Student('Rahul',35)
s3=Student('Priya',65)
print("Student:",s1.name)
print("Marks:",s1.marks)
print("Student:",s2.name)
print("Marks:",s2.marks)

print(s1.is_pass())
print(s2.is_pass())
print(s3.is_pass())
s1.update_marks(45)
print(s1.display())
print(s1.is_pass())
print(s1.marks)
s2.update_marks(45)
print(s2.display())
print(s2.is_pass())
#class method
class Stu :
    college='spc'
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    @classmethod
    def change_college(cls,new):
        cls.college=new
s1 = Stu("Anushka", 90)
s2 = Stu("Rahul", 75)
s3 = Stu("Priya", 85)
Stu.change_college('ABC Engineering College')

print(s1.college)
print(s2.college)
print(s3.college)
s1.college = "PQR"
del s1.college
print(s1.college)

class Calci:
    @staticmethod
    def to_add(n1,n2):
        return n1 + n2
    @staticmethod 
    def to_mul(n1,n2):
        return n1 * n2
    @staticmethod
    def to_sub(n1,n2):
        return n1 - n2
    def to_div(n1,n2):
        if n2 == 0 :
            return 'it cannot divide by zero'
        else:
            return n1 / n2

print(Calci.to_add(98, 79))
print(Calci.to_add(50, 30))
print(Calci.to_mul(20,6))
print(Calci.to_div(50, 30))
print(Calci.to_sub(20,6))

#
class BankAccount:
    def __init__(self,account_number,pin,balance):
        self.account_number=account_number
        self.__pin = pin
        self.__balance=balance
    def get_pin(self):
        return self.__pin
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0 :
            self.__balance = amount + self.__balance
            return self.__balance
        
        else :
            return "Please enter correct amount"

    def withdraw(self,amount):
        if amount > 0 :
            if amount <= self.__balance:
                self.__balance= self.__balance - amount
                return self.__balance
            else:
                return 'insufficient balance'
        else :
            return 'Please try again later'
    def change_pin(self,old_pin,new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return self.__pin
        else :
            return 'incorrect pin '
    def check_balance(self):
        n = print('your current balance is :',self.__balance)
b1 = BankAccount(23344534,2002,1000)
b1.withdraw(4000)
b1.change_pin(2002,2007)
b1.deposit(2000)
print(b1.get_pin())
print(b1.withdraw(500))
print(b1.get_balance())

b1.check_balance()


#inheritance
class Animal:
    def eat(self):
        print('Animal is eating')
class child(Animal):
    def bow(self):
        print('dog bow bow')
d1=child()
d1.eat()
d1.bow()

class Vehicle:
    def start(self):
        print('Vehicle started')
class Car(Vehicle):
    def drive(self):
        print('Car is driving')
c1=Car()
c1.start()
c1.drive()

# #single inheritance
class Person:
    def display_name(self):
        print('My name is anushka')
class Student(Person):
    pass
s1 = Student()
s1.display_name()

# #multiple inheritance
class Python:
    def learn_python(self):
        print("python is very beginner language")
class SQL :
    def learn_sql(self):
        print("Learning sql is very important")
class Developer(Python,SQL):
    pass
l1=Developer()
l1.learn_python()
l1.learn_sql()


# #MULTILEVEL INHERITANCE

class grandparents:
    def grand(self):
        print("they're my grand parents")
class parents(grandparents):
    def parent(self):
        print("they're my parents")
class child(parents):
    def gen(self):
        print("Im a genz kid")
s1 = child()
s1.gen()
s1.grand()
s1.parent()

# #Hierarchical inheritance
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

# #hybrid inheritance
class person:
    def human(self):
        n = input("enter ur name : ")
        print(f"my name is {n}")
class student(person):
    pass
class employee(person):
    pass
class intern(student,employee):
    pass
i = intern()
i.human()

#polymorphism
class car:
    def start(self):
        print("Car engine started")
class bike :
    def start(self):
        print("Bike engine started")
s = car()
b=bike()
s.start()
b.start()

#over riding
class vehicle:
    def start(self):
        print("Vehicle is starting")
class bike(vehicle):
    def start(self):
        print("bike is starting")
c = bike()
c.start()

#super()
class Person:
    def display(self):
        print("I am a person")
class Student(Person):
    def display(self):
        super().display()
        print("Iam a student")
p = Student()
p.display()

#abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPIPayment(Payment):
    def pay(self):
        print("Payment completed using UPI")
p = UPIPayment()
p.pay()
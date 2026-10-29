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
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
    def display(self):
        print('Student : ' , self.name)
        print('Marks : ',self.marks)
        print('Age : ',self.age)
    def is_pass(self):
        return self.marks >= 40
s1=Student('Anushka',90,19)
s2=Student('Rahul',85,18)
print("Student:",s1.name)
print("Marks:",s1.marks)
print("Student:",s2.name)
print("Marks:",s2.marks)
s1.display()
s2.display()
print(s1.is_pass())

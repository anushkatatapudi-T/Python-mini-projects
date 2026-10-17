class Food :
    def __init__(self,food,travel,shopping,rent,beauty,name):
        self.food = food
        self.travel = travel
        self.shopping = shopping
        self.rent = rent
        self.beauty = beauty
        self.name = name
    def to_calc(self):
        return self.food +  self.travel +self.shopping + self.rent +self.beauty
    def display_expenses(self):
        print(f"\n------ {self.name}'s Expenses ------")
        print(f"Food expense: ₹{self.food:.2f}")
        print(f"Travel expense: ₹{self.travel:.2f}")
        print(f"Shopping expense: ₹{self.shopping:.2f}")
        print(f"Rent expense: ₹{self.rent:.2f}")
        print(f"Beauty expense: ₹{self.beauty:.2f}")
        print(f"Total expenses: ₹{self.to_calc():.2f}")

try :
    n = input("Enter your name : ")
    f = float(input("Enter you food expense :  ₹"))
    t = float(input("Enter you travel expense : ₹"))
    s = float(input("Enter you shopping expense : ₹"))
    r = float(input("Enter you rent expense : ₹"))
    b = float(input("Enter you beauty expense : ₹"))
    if min(f, t, s, r, b) < 0:
        print("Expenses cannot be negative.")
    else:
        person = Food(f, t, s, r, b, n)
        person.display_expenses()

except ValueError:
    print("Invalid try to enter numerical value")
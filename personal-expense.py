
expense = []

while True:
    print("\n====== PERSONAL EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Category-wise Spending")
    print("5. Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        name = input("Enter your expense name: ")
        category = input("Enter your category: ")
        amount = float(input("Enter your amount: "))

        expense.append([name, category, amount])
        print("Expenses are added successfully!")

    elif n == 2:
        if len(expense) == 0:
            print("No expenses are added yet.")
        else:
            print("\n-- Your expenses are:")

            for ex in expense:
                print("Name:", ex[0])
                print("Category:", ex[1])
                print("Amount:", ex[2])
                print("------------------")
                

    elif n == 3:
        total = 0

        for ex in expense:
            total = total + ex[2]

        print("Total spending:", total)

    elif n == 4:
        cat = input("Enter category to check: ")
        total = 0

        for ex in expense:
            if ex[1].lower() == cat.lower():
                total = total + ex[2]

        print("Spending in", cat, ":", total)

    elif n == 5:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")

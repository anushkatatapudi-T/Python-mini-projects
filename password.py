
import secrets
import string
holder = []

while True:
    print("\n=== Password Manager ===")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        name = input("Enter your name: ")
        acc = input("Enter your account name: ")
        accno = int(input("Enter your account number: "))
        char =string.ascii_letters + string.digits + "!@#$%&*"
        passw = ""
        for i in range(12) :
            passw = passw +secrets.choice(char)
        print("Generate password : " , passw)
        holder.append([name, acc, accno, passw])
        print("Account added successfully!")

    elif n == 2:
        if len(holder) == 0:
            print("Account is not added yet!")
        else:
            print("--- Your Account Details ---")

            for account in holder:
                print("Name:", account[0])
                print("Account name:", account[1])
                print("Account number:", account[2])
                print("------------------")

    elif n == 3:
        s = input("Enter account name to search: ")
        found = False

        for account in holder:
            if s.lower() == account[1].lower():
                print("--- Account Found ---")
                print("Name:", account[0])
                print("Account name:", account[1])
                print("Account number:", account[2])
                found = True

        if found == False:
            print("Account not found!")

    elif n == 4:
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice! Try again.")

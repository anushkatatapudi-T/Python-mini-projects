try :
    print("Welcome to the calculator")
    num1=float(input("Enter num1:"))
    num2=float(input("Enter num2:"))
    operand = input("Enter an operation(+,-,*,%,/):")
    if operand == "+" :
        print("Result : ",num1+num2)
    elif operand == "-" :
        print("Result : ",num1-num2)
    elif operand == "*" :
        print("Result : ",num1*num2)
    elif operand == "%" :
        if num2 == 0:
            print("Error : cannot find remainder with zero")
        else :
            print("Result : ",num1 % num2)
    elif operand == "/" :
        if num2 == 0 :
            print("Error : cannot divide by zero")
        else :
            print("Result : ",num1/num2)
    else :
        print("Invalid ! input")
except ValueError :
    print("Invalid ! Enter valid input.")


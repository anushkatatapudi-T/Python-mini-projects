print("Welcome ! Student Grade Manager!!")
name = input("Enter your name : ")
m1 = float(input("Enter marks-1 :"))
m2 = float(input("Enter marks-2 :"))
m3 = float(input("Enter marks-3 :"))
t = m1 + m2 + m3
avg = (m1 + m2 + m3) / 3
total = (t/300) * 100
print("\n----Student Result ----")
print("Student name : " , name)
print("Total marks : " , t,"/300")
print("Average marks : " , avg)
print("Percentage : " , total,"%")
if total >= 90 :
    print("Your grade is : Grade-A")
elif total >= 75 :
    print("Your grade is : Grade-B")
elif total >= 65 :
    print("Your grade is : Grade-C")
elif total >= 40 :
    print("Your grade is : Grade-D")
else :
    print("You have failed. Best of luck for your next exam!")

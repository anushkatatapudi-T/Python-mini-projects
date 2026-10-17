
n = int(input("Enter how many students: "))

if n > 0:
    students = []

    for i in range(n):
        print("\nEnter details for Student", i + 1)

        name = input("Enter student's name: ")
        maths = int(input("Enter Maths marks: "))
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
        biology = int(input("Enter Biology marks: "))

        total = maths + physics + chemistry + biology
        avg = total / 4

        students.append([name, maths, physics, chemistry, biology, avg])

        print("Total marks:", total)
        print("Average:", round(avg, 2))

        if avg >= 90:
            print(name, "- Top performance!")
        elif avg >= 70:
            print(name, "- Good performance!")
        else:
            print(name, "- Try to improve!")

    print("\n--- Student Performance Report ---")

    for student in students:
        print("Name:", student[0])
        print("Average:", round(student[5], 2))

    topper = max(students, key=lambda student: student[5])

    print("Topper:", topper[0])
    print("Topper's average:", round(topper[5], 2))

else:
    print("Enter a valid number of students.")

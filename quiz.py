
print("================================")
print("       WELCOME TO THE QUIZ")
print("================================")

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["for", "def", "if", "print"],
        "answer": "def"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input", "type", "print", "len"],
        "answer": "print"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "&"],
        "answer": "#"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "list"],
        "answer": "bool"
    },
    {
        "question": "Which keyword is used for a loop over a list?",
        "options": ["if", "for", "def", "return"],
        "answer": "for"
    }
]

score = 0

for question in questions:
    print("\nQuestion:", question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(i, ".", option)

    while True:
        try:
            n = int(input("Enter your option (1-4): "))

            if n >= 1 and n <= 4:
                break
            else:
                print("Please enter a number from 1 to 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    if question["options"][n - 1] == question["answer"]:
        print("Correct answer!")
        score = score + 1
    else:
        print("Wrong answer!")
        print("Correct answer:", question["answer"])

print("\n================================")
print("          QUIZ RESULTS")
print("================================")
print("Total questions:", len(questions))
print("Correct answers:", score)
print("Wrong answers:", len(questions) - score)
print("Final score:", str(score) + "/" + str(len(questions)))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

print("Thank you for playing!")

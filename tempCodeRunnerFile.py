print("Welcome to the quiz")
question = {
    "question1" : "Which keyword is used to define a function in Python?" ,
    "options" : ["for","def","if","print"] ,
    "answer" : "def"
}
print("Question : ",question["question1"])
print("Options : ",question["options"])
for i,op in enumerate(question["options"],start=1) :
    print(i,".",op)
n = input("Enter the options(1-4) : ")
if n >=1 and n <=4 :
    if question["options"][n-1] == question["answer"] :
        print("Yes! your answer is correct")
    else :
        print("Nope!Try again")
else :
    print("Invalid option! Please enter the correct option from 1 to 4.")

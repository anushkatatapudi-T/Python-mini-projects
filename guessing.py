import random
num = random.randint(1,10)
print("Welcom to number guessing game.!")

guess = int(input("Enter a random number : "))
print("Your guess is..(1-100) : ",guess)
if num == guess :
    print("Yes!Your guess is correct.")
elif num < guess : 
    print("Oop's! too high try again.")
else :
    print("Oop's! Try again its too low")
print("Secret number is :", num)

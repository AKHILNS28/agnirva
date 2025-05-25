import random
num=random.randint(1,100)
print("Welcome to The Number Guessing Game")
print("Can you guess the number correctly")

attempt=0
while (attempt<10):
    k=int(input("Enter your guess"))
    if(k>num):
        print("guess is too high")
    elif(k<num):
        print("guess is too low")
    else:
        print("guess is correct")
        break
import random
print("Welcome to The Number Guessing Game")
print("Can you guess the number correctly")
print("Difficulty levels")
print("1.Easy")
print("2.Medium")
print("3.Hard")
ch=int(input("Choose Difficulty"))
if(ch==1):
    k=random.randint(1,10)
elif(ch==2):
    k=random.randint(1,50)
else:
    num=random.randint(1,100)
attempt=0
while (attempt<10):
    k=int(input("Enter your guess"))
    if(k>num):
        print("guess is too high")
    elif(k<num):
        print("guess is too low")
    else:
        print("guess is correct")
        break;

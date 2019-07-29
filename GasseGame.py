import random

n = 5

while 1 <= n:
    user = int(input("Enter Your Guess Number 1 to 5 : "))
    guessNamber = random.randint(1, 5)
    if user == guessNamber:
        print("You are win. The number is ", guessNamber)
        break
    else:
        print("you are lose. The number is ", guessNamber)
        n = n + 1

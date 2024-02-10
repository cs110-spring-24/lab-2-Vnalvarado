import random
num = random.randint(1, 100)

user = input("Enter your guess: ")
user = int(user)

Count=0
if user > num:
    print("Too high, it was", num)
    Count+=1

Count=1
elif user < num:
    print("Too low, it was", num)
    count+=2

Count=2
else:
    print("You got it!")
    count+=3


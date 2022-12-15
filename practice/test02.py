#!/usr/bin/python3
#guess the correct number
number = 16
guess = -1
print("数字猜谜游戏!")

while (guess != number) :
    guess = int(input("guess what："))

    if guess == number :
        print("Congratulations!")
        break
    elif guess < number :
        print("Too small!")
    else :
        print("Too big!")

input("input enter to exit!")

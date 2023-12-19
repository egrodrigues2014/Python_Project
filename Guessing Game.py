# Guessing Game

import random

while True:
    try:
        level = int(input("Level:"))
        if level > 0:
            break
    except:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess:"))
        if guess < 1:
            continue
    except ValueError:
        pass
    else:
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

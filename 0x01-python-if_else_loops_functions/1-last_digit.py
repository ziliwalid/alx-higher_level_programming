#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDig = abs(number) % 10
if number > 5:
    print(f'Last digit of {number} is {lastDig} and is greater than 5')
elif number == 0:
    print(f'Last digit of {number} is {lastDig} and is 0')
else:
    print(f'Last digit of {number} is -{lastDig} and is less than 6 and not 0')

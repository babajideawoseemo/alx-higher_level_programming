#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last = abs(number) % 10
if number > 5:
print(f"Last digit of {number} is {last} and is greater than 5")
elif number == 0:
    print("Last digit of {nunber} is {last} and is 0")
else:
    print("Last digit of {number} is -{last} and is less than 6 and not 0")

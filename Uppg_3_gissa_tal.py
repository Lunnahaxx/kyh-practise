"""Uppg_8.1 - titta igenom alla program hittills ni byggt i kyh-practice,
och byt ut till f-strings där det behövs.
-
Uppg_3 - gissa tal
Task assignment:
Kod utan tabbar:

import random

n = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. Guess which?")

while True:
text = input("Your guess: ")
as_number = int(text)

if as_number == n:
print("Correct!")
break

if as_number < n:
print("Wrong, my number is higher... Try again!")

if as_number > n:
print("Wrong, my number is lower... Try again!")"""


import random

n = random.randint(1, 20)
print("I'm thinking of a value between 1 and 30. Guess which?")

while True:
    text = input("Your guess: ")
    as_number = int(text)

    if as_number == n:
        print("Correct!")
        break

    if as_number < n:
        print("Wrong, my number is higher.. Try again!")

    if as_number > n:
        print("Wrong, my number is lower... Try again!")
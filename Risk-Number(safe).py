import random
import os

number = random.randint(1, 10)

guess = input("Miłej Gry! Wybierz numer od 1 do 10: ")
guess = int(guess)

if guess == number:
    print("Wygrałeś")
    filename = str(guess)
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Plik o nazwie {filename} został usunięty.")
    else:
        print(f"Plik o nazwie {filename} nie istnieje.")
else:
    print(f"Nie zgadłeś. Prawidłowa liczba to {number}.")

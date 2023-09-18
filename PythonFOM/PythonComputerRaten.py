import os
import random

random_start = 1
random_stop = 100
versuche = 99

user_input = input("Bitte die Zahl eingeben: ")

if not int(user_input):
    print("Du Deep!")
    os.exit(1)

user_input = int(user_input)

if not (0 <= user_input <= 100):
    print("Du Deep!")
    os.exit(2)

computer_random = random.randrange(random_start, random_stop, 1)
for versuch in range(versuche):
    if computer_random == user_input:
        print(f"Versuch: {versuch+1}: Computer hat die Zahl {computer_random} erraten!")
        break
    if computer_random > user_input:
        print(f"Versuch: {versuch+1}: Computer: {computer_random} - groesser als User")
        random_stop = computer_random
    else:
        print(f"Versuch: {versuch+1}: Computer: {computer_random} - kleiner als User")
        random_start = computer_random + 1
        
    computer_random = random.randrange(random_start, random_stop, 1)

    
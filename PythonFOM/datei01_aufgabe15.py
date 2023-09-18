liste = []
for runde in range(1,4):
    input_zahl = int(input(f"Bitte die {runde}. Zahl eingeben: "))
    if input_zahl < 0:
        break;
    liste.append(input_zahl)

for runde in liste:
    print(f"{runde} - {runde**(1/2)}")
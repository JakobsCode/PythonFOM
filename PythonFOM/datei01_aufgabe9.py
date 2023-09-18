keep_running = True
while keep_running:
    jahr = input("Jahr bitte eingeben\n")
    if not jahr.isdigit():
        print("Kein Zahl")
        break
    if int(jahr) == 0:
        print("Ende")
        break
    if int(jahr) == 1:
        continue
    if 1582 <= int(jahr) <= 2015:
        print("Richtig und Wichtig")
        if int(jahr) % 4 == 0 and int(jahr) % 100 != 0 or int(jahr) % 400 == 0:
            print("Schaltjahr")
    else:
        print("LOST")
        continue

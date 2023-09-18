import random
start_random = 1
end_random = 100
geheimzahl = random.randrange(start_random, end_random, 1)
eingabe = 0
zähler = 0
max_versuche = 5

while eingabe != geheimzahl:
    eingabe = int(input("Ganze Zahl eingeben: "))
    zähler+= 1
    
    if zähler >= max_versuche:
        print("MÖÖÖÖP, zu viele Versuche.")
        print(f"Die richtige Zahl wäre {geheimzahl}")
        break
    
    if eingabe < geheimzahl:
        print("Zahl zu klein")
    
    if eingabe > geheimzahl:
        print("Zahl zu groß")

if zähler < max_versuche:
    print("Fertig")
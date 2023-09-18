tastatur = input("Gibt's ein!\n")
länge = len(tastatur)
print(länge)
umfang = None
print(umfang)
if länge < 3:
    umfang = "kurz"
    print("Kleiner 3!")
elif länge <= 10:
    umfang = "kurz"
    print("Zwischen 3 und 10 Zeichen")
else:
    umfang = "lang"
    print("Mehr als 10 Zeichen")   

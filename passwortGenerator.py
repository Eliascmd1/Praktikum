# Schritt 1: Füge die einzelnen Zeichen in der zeichen Variable mithilfe einer for schleife einer Liste hinzu
# Schritt 2: Importiere das Random Modul
# Schritt 3: Fordere den Nutzer dazu auf, eine Passwortlänge anzugeben - achte hier darauf, Fehler abzufangen
# Schritt 4: Schreibe eine Logik, die ein zufälliges Passwort mit der gewünschten Länge generiert - benutze das Random Modul um ein zufälliges Zeichen aus der Liste auszuwählen
# Tipp: benutze random. um herauszufinden, welche Methoden das random Modul bietet oder benutze Stack Overflow

import random

liste = []
passwort = ""
zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
sonderzeichen = "!*&%$/"
passwortliste = []

def checkNumber(input, restriction):
    if input == 0:
        print("Die Zahl darf nicht 0 sein")
        return False
    elif input > restriction:
        print(f"Die Zahl darf nicht größer als {restriction} sein.")
        return False
    return True

def listify(variable):
    for i in variable:
        liste.append(i)

def loopify(question, restriction):
    while True:
        try:
            answer = int(input(question))
            if checkNumber(answer, restriction):
                break
        except:
            print("Du musst eine Zahl eingeben. ")
    return answer
#Passwortstärke: 1. Sonderzeichen? 2. Länger als 8 Zeichen?
# Beides zutreffend -> Starkes Passwort, eines zutreffend -> Mittelstarkes Passwort keines zutreffend -> schwaches passwort
def passwortstaerke():
    specialCharacters = False
    for i in passwort:
        if i in sonderzeichen:
            specialCharacters = True
    if  specialCharacters == True and länge >8 :
        return "Starkes Passwort"
    elif specialCharacters == True or länge > 8:
        return "Mittelstarkes Passwort"
    else:
        return "Schwaches Passwort"


while True:
    mitsonderzeichen = input("Möchtest du in deinem Passwort sonderzeichen haben?(ja/nein) ")
    if mitsonderzeichen.lower() == "ja":
        listify(sonderzeichen)
        break
    elif mitsonderzeichen.lower() == "nein":
        break
    else:
        print("Du musst ja/nein eingeben. ")

listify(zeichen)

passwortanzahl = loopify("Wie viele Passwörter möchtest du generieren? ", 10)

länge = loopify("Wie lang soll das Passwort sein? ", 256)

for i in range(passwortanzahl):
    for i in range(länge):
        passwortZeichen = random.choice(liste)
        passwort =  passwort + passwortZeichen
    print(passwort, end=" ")
    print(passwortstaerke())


    passwortliste.append(passwort)
    passwort = ""

with open("Versuch.txt", "w") as f:
    for i in passwortliste:
        f.write(f"{i}\n")

import random
# variables
liste = []
passwort = ""
zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
sonderzeichen = "!*&%$/"
passwortliste = []
# 1. checknumber function: checks if number is 0 -> prints must be bigger / number too big -> prints must be smaller
def checkNumber(input, restriction):
    if input == 0:
        print("Die Zahl darf nicht 0 sein")
        return False
    elif input > restriction:
        print(f"Die Zahl darf nicht größer als {restriction} sein.")
        return False
    return True
#  listify function: adds variabe to list
def listify(variable):
    for i in variable:
        liste.append(i)
# loopify function: creates loop which checks if userinput is a number + number is in range
def loopify(question, restriction):
    while True:
        try:
            answer = int(input(question))
            if checkNumber(answer, restriction):
                break
        except:
            print("Du musst eine Zahl eingeben. ")
    return answer
# define passwordstrength: 1. condition: password contains special character 2. condition: more than 8 characters
# both conditions true -> strong password, 1 of 2 conditions true -> moderate strong password, none true -> weak password
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

# ask user if password should contain special characters. yes -> use listify function to add them to list
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
# generates and prints password -> chooses random characters out of list
for i in range(passwortanzahl):
    for i in range(länge):
        passwortZeichen = random.choice(liste)
        passwort =  passwort + passwortZeichen
    print(passwort, end=" ")
    print(passwortstaerke())

# adds password to list
    passwortliste.append(passwort)
    passwort = ""
# creates file with list of password.
with open("Versuch.txt", "w") as f:
    for i in passwortliste:
        f.write(f"{i}\n")

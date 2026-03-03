# Bankautomat Programm

# Startbetrag des Kontos
kontostand = 1000

# Dictionary zum Speichern der Transaktionen
transaktionsspeicher = {}

# Festgelegter Pin
pin = "9999"

# 1. Geld abheben:
def abheben():
# Nutzer nach höhe des Betrages fragen + prüfen ob der Nutzer eine Zahl eingegeben hat (Fehler abfangen)
    while True:
        try:
            withdraw = int(input("Wie viel Geld möchtest du abheben?"))
            break
        except:
            print("Du musst eine Zahl eingeben")

# Kontostand global festlegen, damit es auf die Variable ausserhalb der Schleife zugreifen kann
    global kontostand
    speicherlaenge = len(transaktionsspeicher)

# Abfrage ob genug Geld im Konto ist (Kontostand darf nicht negativ sein)
    if (kontostand - withdraw) <0:
        print("Du hast zu wenig Geld.")

# Abheben des betrages mit Transaktionsgebühr
    elif withdraw < 100:
        kontostand -= withdraw + 0.5
        print("Das Geld wurde abgehoben. Es viel eine Gebühr von einem halben Euro an.")
        print(f"Ihr Kontostand beträgt nun {kontostand}.")

# Transaktion wird dem dictionary hinzugefügt
        transaktionsspeicher[speicherlaenge + 1] = {"Art": "Abhebung", "Höhe": withdraw}

# Abheben des Betrages
    else:
        kontostand -= withdraw
        print("Das Geld wurde abgehoben.")
        print(f"Ihr Kontostand beträgt nun {kontostand}.")
        transaktionsspeicher[speicherlaenge + 1] = {"Art": "Abhebung", "Höhe": withdraw}

# 2. Geld einzahlen:
def einzahlen():

# Nutzer nach Höhe des Betrages fragen + prüfen ob der Nutzer eine Zahl eingegeben hat (Fehler abfangen)
    while True:
        try:
            deposit = int(input("Wie viel Geld möchtest du einzahlen?"))
            break
        except:
            print("Du musst eine Zahl eingeben")
    global kontostand
# Prüfen ob Betrag über 10.000 ist + wenn unter 10.000 Betrag hinzufügen
    if deposit > 10000:
        print("Du kannst nicht mehr als 10000 einzahlen.")
    else:
        kontostand += deposit
        print("Das Geld wurde eingezahlt.")
        print(f"Ihr Kontostand beträgt nun {kontostand}.")

# Transaktion dem dictionary hinzufügen
        speicherlaenge = len(transaktionsspeicher)
        transaktionsspeicher[speicherlaenge+1] = {"Art": "Einzahlung", "Höhe": deposit}

# 3. Zurück zu den Auswahlmöglichkeiten kommen
def zurueck():
    back = ""
    while back != "z":
        back = input("Drücke z um zurück zu gelangen.")
        if back == "z":
            break

# 4. Pin abfragen:
for i in range(3):

# Prüfen ob Nutzer eine Zahl eingegeben hat. (Fehler abfangen)
    try:
        pinabfrage = input("Pin eingeben: ")
    except:
        print("Du musst eine Zahl eingeben")

# Prüfen ob Pin richtig ist + nach 3 Versuchen Programm beenden
    if pinabfrage == pin:
        break
    elif i == 2:
        exit()
    else:
        print("Pin ist falsch.")

# 5. Auswahlmöglichkeiten für den Nutzer
while True:
    print("(1) Kontostand anzeigen")
    print("(2) Geld abheben")
    print("(3) Geld einzahlen")
    print("(4) Transaktionshistorie anzeigen")
    print("(5) beenden")
    print("")

# Prüfen ob Nutzer eine Zahl eingegeben hat. (Fehler abfangen)
    try:
        userinput = int(input("Was möchtest du machen?"))
    except:
        print("Du musst eine Zahl eingeben")
        continue

# match-case verwenden
    match userinput:
# Kontostand anzeigen
        case 1:
            print(f"Ihr Kontostand beträgt {kontostand}.")
            print("")
            zurueck()
# abheben
        case 2:
            abheben()
            zurueck()
# einzahlen
        case 3:
            einzahlen()
            zurueck()
# Transaktionen anzeigen
        case 4:
            for i in transaktionsspeicher:
                transaktionsspeicher[i]
                print(i,":", transaktionsspeicher[i])
            zurueck()
# Programm beenden
        case 5:
            print("Programm beendet")
            break
# Alle anderen eingaben abdecken.(Fehler abfangen)
        case _:
            print("Du musst eine Zahl eingeben")
import os

#Funksjon som leser filen og printer den ut i terminalen.
def printTekst():
    file_path = input("Skriv inn navnet på filen du vil søke i. (inkluder .txt): ")
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Funksjon som leter etter ett ord og sier om det er i filen
def sokText():
    file_path = input("Skriv inn navnet på filen du vil søke i. (inkluder .txt): ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word = input("Søk etter ett ord i filen: ")
            if word in content:
                print(f"'{word}' er i filen")
            else:
                print(f"'{word}' er ikke i filen")
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Funksjon som leter etter ett ord og sier om det er i filen med true or false statement i steden for
def sokTrue():
    file_path = input("Skriv inn navnet på filen du vil søke i. (inkluder .txt): ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word = input("Søk etter ett ord i filen: ")
            if word in content:
                print(word in content)
            else:
                print(word in content)
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Funksjon som leter etter hvilken linje ordet er på og printer nummeret på linjen samt linjen
def sokLinje():
    file_path = input("Skriv inn navnet på filen du vil søke i. (inkluder .txt): ")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            word = input("Søk etter ord i filen: ").lower()
            found = False
            for line_number, line in enumerate(lines, start=1):
                if word in line.lower():
                    print(f"'{word}' ble funnet på linje {line_number}: {line.strip()}")
                    found = True
            if not found:
                print(f"'{word}' ble ikke funnet i filen.")
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Fuksjon som sjekker hvor mange av ordet det er i filen
def sokAntall():
    file_path = input("Skriv inn navnet på filen du vil søke i. (inkluder .txt): ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word = input("Søk etter ord i filen: ")
            word_count = content.lower().count(word.lower())
            if word_count > 0 and word_count < 2:
                print(f"'{word}' ble funnet {word_count} gang i filen.")
            elif word_count > 1:
                print(f"'{word}' ble funnet {word_count} ganger i filen.")
            else:
                print(f"'{word}' ble ikke funnet i filen.")
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Funksjon som lar brukeren lage en ny fil og skrive innhold
def lagFil():
    file_path = input("Skriv inn navnet på den nye filen (inkluder .txt): ")
    with open(file_path, 'w') as file:
        content = input("Skriv inn innholdet til filen: ")
        file.write(content)
    print(f"Fil '{file_path}' ble opprettet med innholdet:\n{content}")
    hoved()

#Funksjon som lar brukeren redigere en fil
def redigerFil():
    file_path = input("Skriv inn navnet på filen du vil legge ord til. (inkluder .txt): ")
    try:
        with open(file_path, 'a') as file:
            print("Skriv inn linjer du vil legge til. Trykk Enter på en tom linje for å avslutte.")
            while True:
                content = input()
                if content == "":  #Stopper hvis brukeren trykker enter mens ingenting er skrevet
                    break
                file.write(content + "\n")
        print(f"Innholdet ble lagt til i filen '{file_path}'.")
    except FileNotFoundError:
        print(f"Fil '{file_path}' ble ikke funnet.")
    hoved()

#Funksjon som viser alle filene
def visAlleFiler():
    directory = os.getcwd() #henter directory
    files = os.listdir(directory)
    if files:
        print(f"Filer i katalogen '{directory}':") #kriver hvilke filer som er i directoriet
        for file in files:
            print(f"- {file}")
    else:
        print(f"Katalogen '{directory}' er tom.")
    hoved()

#Funksjonen som printer hovedmenyen og lar brukeren navigere rund samt bruke programmet
def hoved():
    print("------------------- Filsøker -------------------------")
    print("| 1. Print filen.                                    |")
    print("| 2. Søk etter ord i filen.                          |")
    print("| 3. Søk om ord er i filen.                          |")
    print("| 4. Søk om hvilken linje ordet er på.               |")
    print("| 5. Søk om hvor mange ganger ord dukker opp i filen.|")
    print("| 6. Opprett ny fil.                                 |")
    print("| 7. Legg til ord i fil.                             |")
    print("| 8. Vis alle filer i mappa.                         |")
    print("| 9. Avslutt programmet.                             |")
    print("------------------------------------------------------")
    choice = input("Skriv inn ett tall for å velge fra menyen: ")
    if choice == "1":
        printTekst()
    elif choice == "2":
        sokText()
    elif choice == "3":
        sokTrue()
    elif choice == "4":
        sokLinje()
    elif choice == "5":
        sokAntall()
    elif choice == "6":
        lagFil()
    elif choice == "7":
        redigerFil()
    elif choice == "8":
        visAlleFiler()
    elif choice == "9":
        exit()

#starter programmet
hoved()
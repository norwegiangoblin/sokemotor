def printTekst():
    file_path = "sokemotor.txt"
    with open(file_path, 'r') as file:
        print(file.read())
    hoved()

def sokText():
    file_path = "sokemotor.txt"
    with open(file_path, 'r') as file:
        content = file.read()
        word = input("Søk etter ett ord i filen: ")
        if word in content:
            print(f"'{word}' er i filen")
        else:
            print(f"'{word}' er ikke i filen")
    hoved()

def sokTrue():
    file_path = "sokemotor.txt"
    with open(file_path, 'r') as file:
        content = file.read()
        word = input("Søk etter ett ord i filen: ")
        if word in content:
            print(word in content)
        else:
            print(word in content)
    hoved()

def sokLinje():
    file_path = "sokemotor.txt"
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
    hoved()

def sokAntall():
    file_path = "sokemotor.txt"
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
    hoved()

def hoved():
    print("------------------- Filsøker -------------------------")
    print("| 1. Print filen                                     |")
    print("| 2. Søk etter ord i teksten                         |")
    print("| 3. Søk om ord er i teksten                         |")
    print("| 4. Søk om hvilken linje ordet er på                |")
    print("| 5. Søk om hvor mange ganger ord dukker opp i filen |")
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


hoved()
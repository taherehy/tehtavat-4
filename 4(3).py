# Alustetaan lista luvuille
luvut = []

# Kysytään käyttäjältä lukuja, kunnes tyhjä syöte annetaan
while True:
    syote = input("Syötä luku (tyhjä syöte lopettaa): ")

    # Tarkistetaan, onko syöte tyhjä
    if not syote:
        break

    try:
        # Muunnetaan syöte kokonaisluvuksi ja lisätään listaan
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku.")

# Tarkistetaan, onko annettu vähintään yksi luku
if luvut:
    # Tulostetaan pienin ja suurin luku
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")

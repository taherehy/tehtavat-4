# Ohjelma muuntaa tuumat senttimetreiksi
tumat = 0  # Alustetaan muuttuja

while True:
    try:
        # Kysytään käyttäjältä tuumat desimaalilukuna
        tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa ohjelman): "))

        # Tarkistetaan, onko syötetty luku negatiivinen
        if tuumat < 0:
            print("Ohjelma lopetetaan.")
            break

        # Muunnetaan tuumat senttimetreiksi
        senttimetrit = tuumat * 2.54

        # Tulostetaan muunnos kahden desimaalin tarkkuudella
        print(f"{tumat} tuumaa on {senttimetrit:.2f} senttimetriä.")

    except ValueError:
        # Jos käyttäjä syöttää virheellisen arvon (ei desimaaliluku)
        print("Virheellinen syöte. Syötä desimaaliluku.")

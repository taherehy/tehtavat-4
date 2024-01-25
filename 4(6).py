import random

def laske_pi(arvottavien_pisteiden_maara):
    n = 0  # Ympyrän sisälle jäävien pisteiden määrä

    for _ in range(arvottavien_pisteiden_maara):
        # Arvotaan piste neliön sisälle
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Tarkistetaan, onko piste myös yksikköympyrän sisällä
        if x**2 + y**2 < 1:
            n += 1

    # Lasketaan piin likiarvo
    pi_arvio = 4 * n / arvottavien_pisteiden_maara
    return pi_arvio

def main():
    try:
        # Kysytään käyttäjältä arvottavien pisteiden määrä
        arvottavien_pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))

        # Tarkistetaan, että annettu luku on positiivinen
        if arvottavien_pisteiden_maara <= 0:
            print("Syötä positiivinen luku arvottavien pisteiden määräksi.")
        else:
            # Suoritetaan piin likiarvon laskenta
            pi_arvio = laske_pi(arvottavien_pisteiden_maara)

            # Tulostetaan piin likiarvo
            print(f"Piin likiarvo {arvottavien_pisteiden_maara} arvotulla pisteellä on noin {pi_arvio:.6f}.")
    except ValueError:
        print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")

if __name__ == "__main__":
    main()

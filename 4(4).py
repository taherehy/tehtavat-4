import random #moduuli, joka mahdollistaa satunnaislukujen generoinnin.


def arvaa_luku():
    # Arvotaan satunnainen luku väliltä 1..10
    oikea_luku = random.randint(1, 10) #: Arvotaan satunnainen
    # luku väliltä 1..10 ja tallennetaan se oikea_luku-muuttujaan.

    while True: #Aloittaa äärettömän silmukan,
        # joka jatkuu, kunnes break-lauseke suoritetaan.

        try:
            #  Pelaaja antaa arvauksensa, ja se tallennetaan arvaus-muuttujaan.
            arvaus = int(input("Arvaa luku väliltä 1..10: "))

            # Tarkistetaan, onko pelaajan arvaus liian suuri.
            if arvaus == oikea_luku:
                print("Oikein! Arvasit oikean luvun.")
                break
            elif arvaus < oikea_luku: Tarkistetaan, onko pelaajan arvaus liian pieni.
                print("Liian pieni arvaus. Yritä uudelleen.")
            else:  Suoritetaan, jos pelaaja arvasi oikein. Tulostetaan ilmoitus ja
        lopetetaan pelin silmukka #break-lauseella
                print("Liian suuri arvaus. Yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte. Syötä kokonaisluku.")


if __name__ == "__main__":
    arvaa_luku()

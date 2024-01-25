oikea_kayttajatunnus = "python"
#oikea_kayttajatunnus ja oikea_salasana määrittävät oikeat kirjautumistiedot.
oikea_salasana = "rules"
yritykset = 5
#alustetaan viiteen, mikä tarkoittaa, että käyttäjällä on 5 yritystä kirjautua sisään.

while yritykset > 0:
    #-silmukka suoritetaan niin kauan kuin käyttäjällä
    # on yrityksiä jäljellä (yritykset > 0).

    #funktiolla pyydetään käyttäjältä käyttäjätunnus ja salasana.
    kayttajatunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else: #jos tiedot ovat väärin
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
        yritykset -= 1

if yritykset == 0:
    print("Pääsy evätty. Liian monta virheellistä yritystä.")

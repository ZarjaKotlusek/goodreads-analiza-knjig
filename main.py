from zajem_podatkov import (
    zacetek_prenosa,
    pridobi_podatke_knjig,
    shrani_v_csv,
    pridobi_dodatne_podatke,
    shrani_dodatne_podatke,
    CSV_FILENAME
)


def main():

    print("Projekt Goodreads")
    print("1 - Prenesi HTML strani")
    print("2 - Izlušči podatke v CSV")
    print("3 - Poglobljen zajem")
    print("4 - Analiza podatkov")

    izbira = input("Izberi možnost: ")

    if izbira == "1":

        zacetek_prenosa()


    elif izbira == "2":

        podatki = pridobi_podatke_knjig()
        shrani_v_csv(
            podatki,
            CSV_FILENAME
        )


    elif izbira == "3":

        podatki = pridobi_dodatne_podatke()
        shrani_dodatne_podatke(
            podatki
        )


    elif izbira == "4":

        print(
            "Analizo odpri v datoteki analiza.ipynb"
        )


    else:

        print(
            "Neveljavna izbira."
        )


if __name__ == "__main__":
    main()
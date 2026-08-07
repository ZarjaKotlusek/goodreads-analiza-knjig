"""
Projektna naloga: Zajem podatkov o knjigah

Program:
- prenese podatke s spletne strani Goodreads,
- shrani HTML strani,
- iz HTML kode izlušči podatke o knjigah,
- podatke shrani v CSV datoteko.

Podatki, ki jih zajamemo:
- naslov knjige,
- avtor,
- ocena,
- povezava.

"""

import os
import time
import csv
import requests
from bs4 import BeautifulSoup

KNJIGE_MAPA = "knjige"

URL_SEZNAMA = (
    "https://www.goodreads.com/list/show/"
    "6675.The_Guardian_s_1000_Novels_Everyone_Must_Read_"
)

CSV_MAPA = "podatki"

CSV_FILENAME = os.path.join(
    CSV_MAPA,
    "knjige_podrobno.csv"
)


def download_url_to_string(url):
    """
    Prenese spletno stran in vrne njeno HTML vsebino.
    """

    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "Chrome/91.0.4472.124 Safari/537.36",

        "Accept":
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    # Brez glave User-Agent me lahko spletna stran zavrne,
    # saj spletni strežniki preverjajo, kdo jih obiskuje.
    # Program se zato predstavi kot običajen spletni brskalnik.

    try:
        odgovor = requests.get(url, headers=headers)

        # Statusna koda 200 pomeni uspešen prenos.
        if odgovor.status_code == 200:
            return odgovor.text

        print(
            f"Napaka pri prenosu strani. "
            f"Koda: {odgovor.status_code}"
        )

        return None

    except requests.exceptions.RequestException as napaka:

        # Uporabim bolj natančen tip izjeme.
        # Ne želim ujeti vseh možnih napak v programu,
        # ampak samo napake, povezane s knjižnico requests.

        print(f"Napaka pri komunikaciji s strežnikom: {napaka}")

        return None


def save_string_to_file(text, directory, filename):
    """
    Shrani besedilo v datoteko.
    """

    os.makedirs(directory, exist_ok=True)

    pot = os.path.join(directory, filename)

    with open(
        pot,
        "w",
        encoding="utf-8"
    ) as datoteka:

        datoteka.write(text)


def save_page(url, directory, filename):
    """
    Prenese stran in jo shrani.
    """

    vsebina = download_url_to_string(url)

    if vsebina:

        save_string_to_file(
            vsebina,
            directory,
            filename
        )

        print(f"Shranjeno: {filename}")

    else:

        print(f"Napaka pri {url}")


def zacetek_prenosa():
    """
    Prenese vseh 11 strani seznama knjig.
    """

    os.makedirs(
        KNJIGE_MAPA,
        exist_ok=True
    )

    for stran in range(1, 12):

        ime_datoteke = f"stran-{stran}.html"

        pot = os.path.join(
            KNJIGE_MAPA,
            ime_datoteke
        )

        # Če datoteka že obstaja, je ne prenašam ponovno.
        # Tako se izognem nepotrebnim zahtevkom do spletne strani.

        if os.path.exists(pot):

            print(
                f"Datoteka {ime_datoteke} že obstaja, "
                "preskakujem."
            )

            continue

        url = f"{URL_SEZNAMA}?page={stran}"

        print(f"Zajemam {url}...")

        save_page(
            url,
            KNJIGE_MAPA,
            ime_datoteke
        )

        time.sleep(2)

def pridobi_podatke_knjig():
    """
    Prebere vse shranjene HTML strani, iz njih izlušči podatke
    o knjigah in jih shrani v seznam slovarjev.
    """

    vse_knjige = []

    for stran in range(1, 12):

        ime_datoteke = os.path.join(
            KNJIGE_MAPA,
            f"stran-{stran}.html"
        )

        # Če datoteka ne obstaja, jo preskočimo.
        if not os.path.exists(ime_datoteke):
            print(f"Datoteka {ime_datoteke} ne obstaja.")
            continue

        with open(
            ime_datoteke,
            "r",
            encoding="utf-8"
        ) as datoteka:

            vsebina = datoteka.read()

        # HTML pretvorimo v BeautifulSoup objekt.
        juha = BeautifulSoup(
            vsebina,
            "html.parser"
        )

        # Vsaka knjiga je predstavljena z eno vrstico (<tr>).
        vrstice = juha.find_all(
            "tr",
            attrs={"itemscope": ""}
        )

        for vrstica in vrstice:

            naslov_el = vrstica.find(
                "a",
                class_="bookTitle"
            )

            avtor_el = vrstica.find(
                "span",
                itemprop="author"
            )

            ocena_el = vrstica.find(
                "span",
                class_="minirating"
            )

            # Metoda get_text(strip=True) odstrani vse HTML značke
            # in vrne samo besedilo brez odvečnih presledkov.

            knjiga = {

                "naslov":
                    naslov_el.get_text(strip=True)
                    if naslov_el else None,

                "avtor":
                    avtor_el.get_text(strip=True)
                    if avtor_el else None,

                "ocena_raw":
                    ocena_el.get_text(strip=True)
                    if ocena_el else None,

                # href vsebuje povezavo do posamezne knjige.
                "povezava":
                    "https://www.goodreads.com"
                    + naslov_el["href"]
                    if naslov_el else None

            }

            vse_knjige.append(knjiga)

    print(f"Skupaj sem našla {len(vse_knjige)} knjig.")

    return vse_knjige


def shrani_v_csv(podatki, ime_datoteke):
    """
    Shrani zbrane podatke v CSV datoteko.
    """
    os.makedirs(
        CSV_MAPA,
        exist_ok=True
    )
    
    polja = [
        "naslov",
        "avtor",
        "ocena_raw",
        "povezava"
    ]

    with open(
        ime_datoteke,
        "w",
        encoding="utf-8",
        newline=""
    ) as datoteka:

        writer = csv.DictWriter(
            datoteka,
            fieldnames=polja
        )

        # Prva vrstica vsebuje imena stolpcev.
        writer.writeheader()

        # Nato zapišemo vse knjige.
        writer.writerows(podatki)

    print(
        f"Podatki so uspešno shranjeni "
        f"v datoteko '{ime_datoteke}'."
    )

def pridobi_dodatne_podatke(st_knjig=50):
    """
    Za izbrano število knjig obišče posamezno stran knjige
    in pridobi dodatne podatke.

    Privzeto obdela prvih 50 knjig, lahko pa uporabnik
    poda tudi drugo število.
    """

    print("Začenjam poglobljen zajem podatkov ...")

    html = download_url_to_string(f"{URL_SEZNAMA}?page=1")

    if html is None:
        print("Prenos prve strani ni uspel.")
        return []

    juha = BeautifulSoup(html, "html.parser")

    naslovi = juha.find_all(
        "a",
        class_="bookTitle"
    )

    dodatni_podatki = []

    for i, naslov in enumerate(naslovi[:st_knjig], start=1):

        povezava = (
            "https://www.goodreads.com"
            + naslov["href"]
        )

        ime_knjige = naslov.get_text(strip=True)

        print(
            f"Obdelujem knjigo "
            f"{i}/{st_knjig}: {ime_knjige}"
        )

        html_knjige = download_url_to_string(povezava)

        if html_knjige is None:
            continue

        juha_knjige = BeautifulSoup(
            html_knjige,
            "html.parser"
        )

        avtor = None
        opis = None

        element_avtorja = juha_knjige.find(
            "span",
            class_="ContributorLink__name"
        )

        if element_avtorja:
            avtor = element_avtorja.get_text(strip=True)

        element_opisa = juha_knjige.find(
            "span",
            class_="Formatted"
        )

        if element_opisa:
            opis = element_opisa.get_text(
                strip=True
            )

        dodatni_podatki.append({

            "naslov": ime_knjige,
            "avtor": avtor,
            "opis": opis,
            "povezava": povezava

        })

        # Dodamo kratek premor,
        # da ne preobremenimo strežnika.
        time.sleep(1)

    print(
        f"Poglobljen zajem je končan. "
        f"Obdelanih knjig: {len(dodatni_podatki)}"
    )

    return dodatni_podatki

def shrani_dodatne_podatke(podatki):
    """
    Shrani rezultate poglobljenega zajema
    v ločeno CSV datoteko.
    """

    ime_datoteke = "podatki/dodatni_podatki.csv"

    os.makedirs("podatki", exist_ok=True)

    with open(
        ime_datoteke,
        "w",
        encoding="utf-8",
        newline=""
    ) as datoteka:

        polja = [
            "naslov",
            "avtor",
            "opis",
            "povezava"
        ]

        writer = csv.DictWriter(
            datoteka,
            fieldnames=polja
        )

        writer.writeheader()
        writer.writerows(podatki)

    print(
        f"Dodatni podatki so shranjeni v "
        f"'{ime_datoteke}'."
    )
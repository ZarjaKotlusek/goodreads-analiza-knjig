# Projektna naloga: Zajem in analiza podatkov o knjigah

## Opis projekta

V projektni nalogi sem izdelala program za zajem, shranjevanje in analizo podatkov o knjigah s spletne strani Goodreads.

Namen projekta je bil prikazati celoten proces dela s spletnimi podatki:

- pridobivanje podatkov s spletne strani,
- shranjevanje HTML vsebine,
- obdelava HTML kode,
- izluščevanje podatkov o knjigah,
- shranjevanje podatkov v CSV datoteke,
- analiza in vizualizacija rezultatov v Jupyter Notebooku.

Zajeti podatki vključujejo:

- naslov knjige,
- avtorja,
- oceno knjige,
- povezavo do knjige,
- dodatne podatke iz posameznih strani knjig.

---

## Struktura projekta

```
projektna_naloga_koncna/

├── main.py
├── zajem_podatkov.py
├── analiza.ipynb
├── README.md
├── .gitignore
│
├── knjige/
│   └── shranjene HTML strani
│
└── podatki/
    ├── knjige_podrobno.csv
    └── dodatni_podatki.csv
```

---

## Opis posameznih datotek

### main.py

Datoteka predstavlja glavni program projekta.

Omogoča izbiro posameznih korakov:

1. prenos HTML strani,
2. izluščitev podatkov in shranjevanje v CSV datoteko,
3. poglobljen zajem dodatnih podatkov,
4. zagon analize.

---

### zajem_podatkov.py

Modul vsebuje funkcije za pridobivanje podatkov.

V datoteki so vključeni:

- prenos spletnih strani s knjižnico `requests`,
- shranjevanje HTML strani,
- obdelava HTML kode s knjižnico `BeautifulSoup`,
- izluščitev podatkov o knjigah,
- poglobljen zajem podatkov posameznih knjig,
- shranjevanje rezultatov v CSV datoteke.

---

### analiza.ipynb

Jupyter Notebook vsebuje analizo pridobljenih podatkov.

V njem so izvedeni:

- uvoz podatkov,
- pregled podatkovne strukture,
- čiščenje ocen,
- izračun povprečnih vrednosti,
- analiza porazdelitve ocen,
- grafični prikazi,
- analiza povezave med dolžino naslova in oceno,
- analiza avtorjev,
- pregled manjkajočih podatkov.

Rezultati analiz so predstavljeni tabelarično in grafično.

---

## Uporabljene knjižnice

Pri izdelavi projekta sem uporabila naslednje Python knjižnice:

- `requests`  
  za prenos spletnih strani,

- `beautifulsoup4`  
  za razčlenjevanje HTML kode,

- `pandas`  
  za obdelavo in analizo podatkov,

- `matplotlib`  
  za izdelavo grafov.

---

## Namestitev knjižnic

Pred zagonom projekta je potrebno namestiti uporabljene knjižnice:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

---

## Zagon projekta

Glavni program se zažene z ukazom:

```bash
python main.py
```

Po zagonu uporabnik izbere želeni korak obdelave podatkov.

Analiza rezultatov se izvede v datoteki:

```text
analiza.ipynb
```

---

## Vir podatkov

Podatki so pridobljeni s spletne strani Goodreads.

Vir:

https://www.goodreads.com/

---

## Cilj projekta

Cilj projektne naloge je bil prikazati uporabo programiranja pri delu s spletnimi podatki.

Projekt vključuje:

- spletno pridobivanje podatkov,
- delo z datotekami,
- obdelavo tabelaričnih podatkov,
- statistično analizo,
- vizualizacijo rezultatov.
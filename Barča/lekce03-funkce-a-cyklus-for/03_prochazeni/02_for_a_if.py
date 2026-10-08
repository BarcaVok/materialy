# ---------------------------------------------
#  Podmínka uvnitř cyklu
# ---------------------------------------------
# Do cyklu můžeme dát if – rozhodne se u KAŽDÉHO průchodu zvlášť.
# Odsazení hlídá, co kam patří: if je uvnitř cyklu, jeho tělo ještě víc.
# Spusť soubor a sleduj výsledky.


# Vypiš jen sudá čísla od 1 do 10:
for cislo in range(1, 11):
    if cislo % 2 == 0:
        print(cislo)          # 2, 4, 6, 8, 10


# Podmínka + počítadlo z minulé složky = spočítáme, kolik jich je.
# Kolik sudých čísel je od 1 do 20?
pocet = 0
for cislo in range(1, 21):
    if cislo % 2 == 0:
        pocet = pocet + 1
print("sudých čísel:", pocet)     # 10


# Šikovný pomocník: zápis  pismeno in "aeiou"  zjistí, jestli je písmeno
# jedno z těch v uvozovkách (vrátí True/False). V cyklu se skvěle hodí –
# třeba spočítat samohlásky ve slově:
slovo = "ananas"
samohlasky = 0
for pismeno in slovo:
    if pismeno in "aeiou":
        samohlasky = samohlasky + 1
print("samohlásek:", samohlasky)  # 3

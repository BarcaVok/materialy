# ---------------------------------------------
#  continue – přeskoč zbytek průchodu
# ---------------------------------------------
# Spusť soubor a zadej pár čísel, mezi nimi i nějaké záporné.
#
# break z cyklu vyskočí úplně. Příkaz continue ukončí jenom jeden průchod:
# zbytek těla cyklu se přeskočí a pokračuje se kontrolou podmínky.


# Sčítáme zadaná čísla, záporná do součtu nepočítáme.
soucet = 0
while True:
    odpoved = input("Zadej číslo (nebo 'konec'): ")
    if odpoved == "konec":
        break
    cislo = int(odpoved)
    if cislo < 0:
        print("Záporné číslo přeskakujeme.")
        continue          # zpátky nahoru, další řádky se neprovedou
    soucet = soucet + cislo
    print("Zatím máme:", soucet)
print("Součet:", soucet)


# Pozor na continue v cyklu s počítadlem. Tenhle cyklus by běžel
# donekonečna – u trojky se continue vrátí nahoru a řádek, který cislo
# zvětšuje, se přeskočí (NESPOUŠTĚJ):
#
# cislo = 1
# while cislo <= 5:
#     if cislo == 3:
#         continue
#     print(cislo)
#     cislo = cislo + 1

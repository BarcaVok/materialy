# ---------------------------------------------
#  Sbírání výsledku v cyklu
# ---------------------------------------------
# V minulé složce jsme součet čísel udělali funkcí sum. Teď si ukážeme,
# jak k němu cyklus dojde „ručně" – krok za krokem. Tenhle trik se hodí
# pokaždé, když v cyklu něco postupně sbíráme.
# Spusť soubor a sleduj výsledky.


# Trik: máme proměnnou a v každém kroku do ní něco přidáme.
# U sčítání začínáme na nule.
soucet = 0
for cislo in range(1, 6):
    soucet = soucet + cislo   # k dosavadnímu součtu přičti aktuální číslo
print(soucet)                 # 15   protože 1 + 2 + 3 + 4 + 5
# (Krok za krokem to ukazuje obrázek cyklus_for_soucet_vizualizace.png.)

# Počítadlo – kolikrát se něco stalo. Přičítáme pořád jedničku:
pocet = 0
for cislo in range(10):
    pocet = pocet + 1
print("cyklus proběhl", pocet, "krát")    # 10


# Násobení v cyklu. Pozor – u násobení musíme začít na jedničce,
# ne na nule – násobení nulou by dalo vždycky nulu.
# Takhle spočítáme 1 * 2 * 3 * 4:
soucin = 1
for cislo in range(1, 5):
    soucin = soucin * cislo
print(soucin)                 # 24

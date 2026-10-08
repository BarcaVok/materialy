# ---------------------------------------------
#  for a range: různé rozsahy
# ---------------------------------------------
# range známe z minulé složky. V cyklu for ho teď využijeme naplno –
# určuje, přes která čísla cyklus projde.
# Spusť soubor a sleduj výsledky.


# range od-do: čísla od prvního čísla do druhého (druhé se NEpočítá).
for cislo in range(1, 6):
    print(cislo)              # 1, 2, 3, 4, 5


# range s krokem: range(od, do, krok) – o kolik se skáče.
# Tímhle vypíšeme sudá čísla:
for cislo in range(0, 10, 2):
    print(cislo)              # 0, 2, 4, 6, 8


# Proměnnou z cyklu můžeme rovnou použít ve výpočtu:
for cislo in range(1, 6):
    print(cislo, "na druhou je", cislo * cislo)


# Důležité: co je odsazené, patří dovnitř cyklu a opakuje se.
# Co je pod cyklem BEZ odsazení, se provede až potom – jednou.
for cislo in range(3):
    print("uvnitř cyklu:", cislo)
print("hotovo")              # vypíše se jednou, až cyklus doběhne

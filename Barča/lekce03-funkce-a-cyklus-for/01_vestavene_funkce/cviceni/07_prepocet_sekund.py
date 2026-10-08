# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.


sekundy = int(input("Zadej sekundy: "))

hodiny = sekundy // 3600
minuty = sekundy % 3600 // 60
zbytek = sekundy % 3600

print(hodiny, minuty, zbytek, sep=":")
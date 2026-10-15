# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.

soucet = 0
cislo = int(input("Zadej číslo: "))

while cislo != 0:
    soucet = soucet + cislo
    print(soucet)
    cislo = int(input("Zadej číslo: "))
    
print(soucet)

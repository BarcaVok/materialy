# Bonus 3 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.


prvni = int(input("Zadejte číslo: "))
druhe = int(input("Zadejte číslo: "))
treti = int(input("Zadejte číslo: "))

print(max(prvni, druhe, treti))
print(min(prvni, druhe, treti))
print((prvni + druhe + treti) < 1000)

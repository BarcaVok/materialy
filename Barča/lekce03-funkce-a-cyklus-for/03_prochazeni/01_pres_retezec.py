# ---------------------------------------------
#  Procházení textu
# ---------------------------------------------
# Cyklus for umí projít nejen čísla z range, ale i písmena v textu.
# Napíšeme for pismeno in slovo: a proměnná se postupně nastaví
# na každé písmeno – jedno po druhém.
# Spusť soubor a sleduj výsledky.


# Projdeme slovo znak po znaku:
slovo = "Ahoj"
for pismeno in slovo:
    print(pismeno)        # A, h, o, j – každé na svůj řádek


# Proměnnou si můžeme pojmenovat jakkoli – tady třeba znak.
# A funguje to na jakýkoli text, klidně i od uživatele:
jmeno = input("Napiš svoje jméno: ")
for znak in jmeno:
    print(znak, "!")

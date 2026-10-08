# ---------------------------------------------
#  Podmínka na vstup od uživatele
# ---------------------------------------------
# Spusť soubor a vyzkoušej ho víckrát s různými čísly.
#
# Teď spojíme dohromady všechno: vstup od uživatele (input z minula)
# a rozhodování (if). Program se zeptá a podle odpovědi zareaguje.


# Vzpomeň si na čtverec z minulé lekce. Tehdy jsme stranu psali napevno.
# Teď ji necháme zadat uživatele – a ověříme, že dává smysl.
strana = float(input("Zadej stranu čtverce v centimetrech: "))

if strana > 0:
    print("Obvod je", 4 * strana, "cm")
    print("Obsah je", strana * strana, "cm²")
else:
    print("Strana musí být kladné číslo.")

# Zkus program spustit dvakrát: jednou zadej 5, podruhé -3.
# Uvidíš, že se pokaždé provede jiná větev.


# Nezapomeň na převod: input() vrací vždycky text. Kdybychom napsali
# jen strana = input(...), byl by v proměnné text "5", ne číslo 5,
# a počítat by s ním nešlo. Proto ho převádíme na číslo pomocí float().

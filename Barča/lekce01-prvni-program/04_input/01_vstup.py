# ---------------------------------------------
#  Vstup od uživatele (input)
# ---------------------------------------------
# Zatím jsme všechno psali napevno do kódu. Funkce input umí
# program „oživit" – zeptá se uživatele a počká, až něco napíše.
#
# Spusť soubor a odpověz na otázku dole v terminálu.
# Pozor: po spuštění to vypadá, že se nic neděje – program ale
# čeká, až něco napíšeš do terminálu a stiskneš Enter.


# input zobrazí otázku a to, co uživatel napíše,
# si uložíme do proměnné:
jmeno = input("Jak se jmenuješ? ")
print("Ahoj,", jmeno)


# Zeptat se můžeme i na víc věcí:
mesto = input("A odkud jsi? ")
print(jmeno, "z města", mesto, "– vítej!")

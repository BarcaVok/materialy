# Cvičení 5 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program má sečíst číslice v PINu a vypsat jedno číslo –
# konečný součet. Teď vypisuje čtyři řádky.
#
# Nápověda: dej breakpoint na řádek s printem a mačkej Continue.
# Kolikrát se na něm program zastaví?

pin = "4821"

soucet = 0

for znak in pin:
    soucet = soucet + int(znak)
    print(f"Součet číslic: {soucet}")

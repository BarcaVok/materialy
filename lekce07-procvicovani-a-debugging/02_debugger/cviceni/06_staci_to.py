# Cvičení 6 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program se zeptá, kolik máš korun a kolik stojí vstupenka,
# a řekne, jestli ti to stačí.
#
# Zadej 1000 a 250.
#
# Nápověda: obě čísla vypadají ve výpisu správně. Zastav program
# breakpointem a podívej se na ně v panelu Variables. Všimni si
# uvozovek.

castka = input("Kolik korun máš? ")
cena = input("Kolik stojí vstupenka? ")

if castka > cena:
    print("Stačí.")
else:
    print("Nestačí.")

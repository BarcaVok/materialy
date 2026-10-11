# Řešení cvičení 6 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V téhle funkci je chyba. Spusť soubor, přečti si hlášku a funkci
#    oprav. Zbytek programu nech tak, jak je.
#    print hodnotu jen ukáže na obrazovce a funkce pak vrací None.
#    Sčítat None nejde, proto TypeError. S return se dá s výsledkem
#    dál počítat.

def obvod_ctverce(strana):
    return strana * 4


celkem = obvod_ctverce(3) + obvod_ctverce(5)
print("Dohromady:", celkem)

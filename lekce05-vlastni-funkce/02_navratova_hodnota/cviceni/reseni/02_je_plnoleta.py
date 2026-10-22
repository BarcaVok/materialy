# Řešení cvičení 2 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".

def je_plnoleta(vek):
    return vek >= 18


# Porovnání vek >= 18 vyrobí True nebo False samo. Delší zápis, který
# dělá to samé a čte se snadněji:
#
# def je_plnoleta(vek):
#     if vek >= 18:
#         return True
#     else:
#         return False


vek = int(input("Kolik ti je let? "))
if je_plnoleta(vek):
    print("Můžeš dál.")
else:
    print("Ještě ne.")

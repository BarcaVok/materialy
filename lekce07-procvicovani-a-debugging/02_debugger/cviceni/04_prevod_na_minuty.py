# Cvičení 4 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program sečte délku tří tréninků zadaných ve tvaru "h:mm".
# Zkus funkci nejdřív na "0:45". Nula hodin a pětačtyřicet minut
# je pětačtyřicet minut – u takového vstupu se splést nedá.
#
# Nápověda: chyba je uvnitř funkce. Dej breakpoint na její první
# řádek a pak mačkej Step Over.

def na_minuty(cas):
    hodiny = int(cas[0])
    minuty = int(cas[2:3])
    return hodiny * 60 + minuty


pondeli = na_minuty("2:45")
streda = na_minuty("1:30")
patek = na_minuty("2:20")

celkem = pondeli + streda + patek

print(f"Pondělí: {pondeli} min")
print(f"Středa:  {streda} min")
print(f"Pátek:   {patek} min")
print(f"Celkem:  {celkem} min")

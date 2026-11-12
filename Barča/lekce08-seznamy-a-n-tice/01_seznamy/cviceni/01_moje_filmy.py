# Cvičení 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Vytvoř seznam pěti svých oblíbených filmů. Vypiš:
#    - první film,
#    - poslední film,
#    - první tři filmy jako výřez,
#    - všechny filmy, každý na vlastní řádek s pomlčkou na začátku,
#    - kolik filmů v seznamu je.



filmy = ["Co děláme v temnotách", "Hercules Poirot", "Shrek", "Wicked", "Madagaskar"]

print(filmy[0])
print(filmy[-1])

print(filmy[0:3])

for film in filmy:
    print(f"-{film}")
    
print(len(filmy))
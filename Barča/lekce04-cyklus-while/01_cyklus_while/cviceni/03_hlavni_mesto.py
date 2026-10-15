# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".

mesto = input("Jaké je hlavní město? ")

while mesto != "Praha":
    print("Špatně!")
    mesto = input("Jaké je hlavní město? ")
print("Správně, je to: ", mesto)    


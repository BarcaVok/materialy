# Řešení cvičení 5 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš program, který pořád dokola nabízí tři možnosti a zeptá se,
#    co má udělat:
#
#      1 - hodit kostkou
#      2 - pozdravit
#      3 - konec
#
#    Volba 1 hodí kostkou a vypíše, co padlo. Volba 2 se zeptá na jméno
#    a pozdraví ho. Volba 3 program ukončí. Po volbě 1 a 2 se nabídka
#    objeví znovu. Na cokoli jiného program odpoví, že volbu nezná.
#    Použij cyklus while True.
#    Zobrazení nabídky i obě akce napiš jako vlastní funkce.

from random import randrange

def zobraz_menu():
    print("1 - hodit kostkou")
    print("2 - pozdravit")
    print("3 - konec")


def hod_kostkou():
    print("Padlo:", randrange(1, 7))


def pozdrav(jmeno):
    print("Ahoj,", jmeno)


while True:
    zobraz_menu()
    volba = input("Co chceš dělat? ")
    if volba == "1":
        hod_kostkou()
    elif volba == "2":
        jmeno = input("Koho pozdravit? ")
        pozdrav(jmeno)
    elif volba == "3":
        break
    else:
        print("Takovou volbu neznám.")
print("Nashledanou!")

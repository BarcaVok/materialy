# ---------------------------------------------
#  Co je funkce
# ---------------------------------------------
# Funkce je pojmenovaná operace – kus hotové práce, který za nás Python
# udělá, když ho zavoláme jménem. Vlastně je používáme už od první lekce,
# jen jsme jim tak neříkali: print, input i int jsou všechno funkce.
#
# Jak se funkce používá:
#   1. Napíšeme její jméno a za něj závorky ( ).
#   2. Do závorek můžeme dát vstup – říká se mu argument (třeba text
#      nebo číslo). Kolik argumentů funkce chce, je u každé jiné:
#      některé žádný nepotřebují, jiné vyžadují jeden a některé jich
#      berou i víc. Sama si to určíš, až budeš psát vlastní funkce.
#   3. Funkce něco udělá. A jsou dva druhy:
#        - buď nám VRÁTÍ výsledek, který si uložíme a dál s ním pracujeme,
#        - nebo jen něco provede a žádnou užitečnou hodnotu zpět nedá.
#
# Spusť soubor a projdi si příklady obou druhů.


# --- Funkce, která jen něco udělá ---

# print vypíše text na obrazovku. Argument je to, co má vypsat.
# Zpátky nám nic užitečného nedá – jen to vypíše.
print("Ahoj")


# print umí přijmout i víc argumentů najednou, oddělených čárkou.
# Mezi ně sám doplní mezeru.
print("Ahoj", "Anno", 2025)     # Ahoj Anno 2025


# Některé funkce mají i pojmenované argumenty – napíšeme u nich jméno
# a rovnítko. print jich má dva užitečné: sep a end.

# sep určuje, co se vypíše MEZI argumenty (místo mezery):
print(2, 3, 4, sep=", ")        # 2, 3, 4

# end určuje, co se vypíše NA KONCI (místo přechodu na nový řádek).
# Tyhle dva printy proto skončí na jednom řádku vedle sebe:
print("Ahoj", end=" ")
print("světe")                  # Ahoj světe


# --- Funkce, které nám VRÁTÍ hodnotu ---

# input se zeptá uživatele a jeho odpověď nám vrátí (jako text).
# Proto si ji ukládáme do proměnné.
jmeno = input("Jak se jmenuješ? ")
print("Ahoj,", jmeno)


# int převede text na číslo a to číslo vrátí. Taky ho známe z minula.
odpoved = input("Kolik ti je let? ")   # input vrátí text, třeba "30"
vek = int(odpoved)                     # int z textu udělá číslo 30
print("Za rok ti bude", vek + 1)

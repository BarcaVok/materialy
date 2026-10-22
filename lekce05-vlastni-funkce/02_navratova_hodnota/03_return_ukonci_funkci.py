# ---------------------------------------------
#  return funkci ukončí
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Jakmile Python narazí na return, funkci opustí. Řádky pod ním
# se už neprovedou:

def pozdrav_a_vrat(jmeno):
    print("Zdravím,", jmeno)
    return "hotovo"
    print("Tenhle řádek se nikdy nevypíše.")


print(pozdrav_a_vrat("Anno"))


# return jde napsat i bez hodnoty. Pak funkci jenom ukončí. Hodí se, když
# se zbytek práce nemá dělat vůbec:
def pozdrav(jmeno):
    if jmeno == "":
        print("Nevím, koho zdravit.")
        return
    print("Ahoj,", jmeno)
    print("Vítej v kurzu!")


pozdrav("Anno")


# Takový return žádnou hodnotu nepředá, takže funkce vrátí None – stejně
# jako funkce, která return nemá vůbec.
print(pozdrav(""))


# Funkce může mít returnů víc. Použije se ten, ke kterému program dojde
# jako k prvnímu – takhle si funkce vybírá z několika odpovědí:
def ohodnot_znamku(znamka):
    if znamka == 1:
        return "Výborně"
    elif znamka == 2:
        return "Chvalitebně"
    elif znamka == 3:
        return "Dobře"
    else:
        return "Ještě zabereme"


for znamka in range(1, 6):
    print(znamka, "->", ohodnot_znamku(znamka))


# Tuhle funkci jsi psala i v minulé složce, tam ale hodnocení rovnou
# vypisovala. Teď ho vrací, takže si volající může vybrat, co s ním –
# vypsat ho, uložit, nebo poslat do další funkce.
hodnoceni = ohodnot_znamku(1)
print("Na vysvědčení bude:", hodnoceni)

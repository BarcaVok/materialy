# ---------------------------------------------
#  Proč cyklus while
# ---------------------------------------------
# Spusť soubor a vyzkoušej ho víckrát s různými odpověďmi.
# Když budeš chtít program zastavit dřív, klikni dole do panelu Terminál
# a zmáčkni Ctrl+C. Program jde taky zabít ikonou koše vpravo v tom panelu.
#
# Cyklus for použijeme, když předem víme, kolikrát se má něco zopakovat –
# projdeme range nebo písmena ve slově. Někdy to ale předem nevíme.
# Chceme opakovat „dokud něco platí". Od toho je cyklus while.


# Ptáme se na heslo tak dlouho, dokud není správné.
heslo = input("Zadej heslo: ")
while heslo != "pyladies":
    print("Špatně, zkus to znovu.")
    heslo = input("Zadej heslo: ")
print("Vítej!")


# Na heslo se ptáme dvakrát – jednou před cyklem, jednou uvnitř. Není to
# překlep. 
# Před cyklem se musíme zeptat proto, aby podmínka měla co porovnávat: kontroluje se
# dřív, než tělo cyklu poprvé proběhne. 
# Uvnitř proto, aby se odpověď před další kontrolou změnila. 
# Bez toho by heslo zůstalo pořád stejné, podmínka by pořád platila a cyklus by běžel donekonečna.
# Tomuhle dvojímu ptaní se nevyhneš u žádného cyklu,
# který se na něco ptá. (V souboru 04 uvidíš, jak jde obejít.)


# Kolikrát se cyklus zopakoval? To dopředu nevíme – záleží na tom,
# kdy heslo trefíš. Napoprvé, napotřetí, nebo až po deseti pokusech.
# Cyklus for potřebuje počet opakování předem, takže tohle nezvládne.
# Cyklu while stačí podmínka.


# Takhle se cyklus while čte:
#   while     = klíčové slovo (opakuj, dokud...)
#   podmínka  = výsledkem je True/False, stejně jako u if z lekce 2
#   :         = dvojtečka na konci řádku
#   odsazení  = odsazené řádky patří dovnitř cyklu a opakují se
#
#   while heslo != "pyladies":
#       ...odsazené řádky...
#
# (Celý cyklus krok za krokem ukazuje obrázek cyklus_while.png.)

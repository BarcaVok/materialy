# Bonus 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci vyhodnot_vysvedceni, která má na vstupu seznam známek
#    a vrátí text:
#
#      "bez známek"             když je seznam prázdný
#      "neprospěl/a"            když je mezi známkami pětka
#      "s vyznamenáním"         když je průměr nejvýš 1.5 a žádná známka
#                               není horší než 2
#      "prospěl/a"              jinak
#
#    Vyzkoušej ji na seznamech [1, 2, 1], [1, 3, 2], [1, 5, 1] a [].


def vyhodnot_vysvedceni(seznam_znamek):
    
    if seznam_znamek == 0:
        return "bez známek"
    prumer = sum(seznam_znamek)/len(seznam_znamek)
    if 5 in seznam_znamek:
        print("neprospěl/a" )
    if prumer <= 1.5 and max(seznam_znamek):
        print("s vyznamenáním"  )
    else:
        print("prospěl/a" )
        
vyhodnot_vysvedceni([1, 2, 1])
vyhodnot_vysvedceni([1, 3, 2])
vyhodnot_vysvedceni( [1, 5, 1] )
vyhodnot_vysvedceni([])

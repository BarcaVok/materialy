# print(range(1,10))

# max_hodnota = 10

# for cislo in range(1, 10):
#         print("Aktuální číslo je: ", cislo)
        


# def vypisCisel(max_hodnota, jmeno_volani, ukaz_caru=True):
#     for aktualni_cislo in range(1, max_hodnota):
#         print(jmeno_volani, ":", aktualni_cislo)   
#     if ukaz_caru:
#         print("-"*30)     


# vypisCisel(10, "Volani A")
# vypisCisel(100, "Volani B", False)


def cena_mhd(vek):
    # print("Počítám cenu lístků pro věk", vek)
    if vek < 6:
        # print("Cena 0")
        return 0
    elif vek < 18:
        # print("39")
        return 39
    elif vek < 65:
        # print("50")
        return 50
    else:
        # print("Cena O")
        return 0
        
# cena_mhd(77)
    
zustatek_uctu = 100
cena_jizdenky = cena_mhd(7)
zustatek_uctu = zustatek_uctu - cena_jizdenky

print(zustatek_uctu)
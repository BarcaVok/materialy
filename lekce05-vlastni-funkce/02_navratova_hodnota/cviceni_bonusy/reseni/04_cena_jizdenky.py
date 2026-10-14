# Řešení bonusu 4 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci cena_jizdenky, která má na vstupu věk cestujícího
#     a základní cenu jízdenky, a vrátí cenu, kterou cestující zaplatí:
#
#       děti do 10 let včetně       zdarma
#       mládež do 18 let včetně     polovina
#       senioři od 65 let včetně    třetina
#       ostatní                     plná cena
#
#     Vyzkoušej ji pro několik věků a ceny vypiš.
#     Podmínky se zkouší odshora. Jakmile jedna platí, funkce se vrátí
#     a na další už nedojde – proto stačí u mládeže napsat vek <= 18.
#     Desetileté a mladší totiž zachytil už první if.

def cena_jizdenky(vek, cena):
    if vek <= 10:
        return 0
    elif vek <= 18:
        return cena / 2
    elif vek >= 65:
        return cena / 3
    else:
        return cena


print("8 let:", cena_jizdenky(8, 30))
print("10 let:", cena_jizdenky(10, 30))
print("15 let:", cena_jizdenky(15, 30))
print("40 let:", cena_jizdenky(40, 30))
print("70 let:", cena_jizdenky(70, 30))

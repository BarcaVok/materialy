# hoste = ["Marta", "Shrek", "Petr Pavel"]

# pocet_hostu = len(hoste)
# # print(hoste)

organizator = "Karel Gott"

# organizator = organizator.upper() + "Gott"

# # print(f"{organizator} zve {hoste} na vánoční večírek.")

# # print(f"Na večírek je pozváno, {len(hoste)}. hostů.")


# pozvanka = "Zvu vás na svůj vánoční večírek."


# # for host in range(pocet_hostu):
# #     print(f"Zveme Vá na vánoční večírek {hoste[host]}")
    
    
# blacklist = ["Hegerová", "Vlk"]


# prichozi = input("Jak se jmenuješ?")

# def kontrola(prichozi, hoste, blacklist):
#     if prichozi in hoste:
#         print("Vstupte!")
#     elif prichozi in blacklist:
#         print("Zmiz nebo se neznám!")
#     else:
#         print("Vstup zakázán.")
        
# kontrola(prichozi, hoste, blacklist)
# hoste = ["Marta", "Shrek", "Petr Pavel"]
# def pozvi(jmeno, hoste):
#     hoste.append(jmeno)

# pozvi("Vojta", hoste)
# print(hoste)
# hoste[5:6] = ["Tom", "Vojta"]
# print(hoste)
# hoste[0] = "Martina"
# print(hoste)

rozdelene_jmeno = organizator.split()
inicialy = ""
for i in rozdelene_jmeno:
    inicialy = inicialy + i[0]
    print(inicialy)

rozdelene_jmeno = organizator.split()
inicialy = []
for i in rozdelene_jmeno:
    inicialy.append(i[0])
    print("-".join(inicialy))
    
# rozdelene_jmeno = organizator.split()[0][0]
# print(rozdelene_jmeno)



hoste = ["Marta", "Shrek", "Petr Pavel"]

def odeber_hosta(jmeno, hoste):
    hoste.remove(jmeno)

odeber_hosta("Shrek", hoste)
print(hoste)

fronta = ["Vojta", "Petra", "Oslík", "Shrek"]


fronta.pop()


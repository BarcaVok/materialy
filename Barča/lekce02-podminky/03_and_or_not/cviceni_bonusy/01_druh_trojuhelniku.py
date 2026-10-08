# Bonus 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Druh trojúhelníku. Máš tři strany. Urči a vypiš, jaký to je
#     trojúhelník:
#       - "rovnostranný", když jsou všechny tři strany stejné,
#       - "rovnoramenný", když jsou aspoň dvě strany stejné,
#       - "různostranný", když jsou všechny strany různé.

a = 5
b = 5
c = 8

if a == b and a == c:
    print("rovnostranný")
elif (a == b) or (a == c) or (b == c):
    print("rovnoramenný")
else:
    print( "různostranný")
# ---------------------------------------------
#  Chybová hláška (co se stane, když uděláš chybu)
# ---------------------------------------------
# Dělat chyby je úplně normální – dělají je i zkušení programátoři.
# Když něco napíšeš špatně, Python program zastaví a vypíše
# chybovou hlášku. Není to nic zlého, jen ti říká, co je špatně.
#
# Zkus tenhle soubor spustit. Objeví se chyba – to je schválně!


# Na řádku níž chybí uvozovky kolem textu:
print(Máma má mísu)


# V terminálu uvidíš něco podobného:
#
#   File "04_chybova_hlaska.py", line 12
#       print(Máma má mísu)
#                  ^^^
#   SyntaxError: invalid syntax
#
# Chybová hláška ti řekne:
#   - ve kterém souboru chyba je,
#   - na kterém řádku,
#   - a jaký druh chyby to je (třeba SyntaxError).
#
# Jak to opravit?
# Dej text do uvozovek:  print("Máma má mísu")
# a spusť soubor znovu. Chyba zmizí. 
#
# Chybovým hláškám se budeme víc věnovat později. Teď stačí vědět,
# že jsou normální a že se dají přečíst.

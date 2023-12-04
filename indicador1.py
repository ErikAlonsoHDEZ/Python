indicador = False
for var in range (1,6):
    num = int(input("Dime un número:"))
    if num % 2 == 0:
        indicador = True
if indicador:
    print("Has introducido algún numero par")
else:
    print("No has introducido algún número par")
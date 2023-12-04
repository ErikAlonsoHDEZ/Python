nombre = input("Dime tu nombre:")
apellido1 = input("Dime tu primer apellido:")
apellido2 = input("Dime tu segundo apellido:")
inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]
inicial = inicial.upper()
print("Las iniciales son:", inicial)
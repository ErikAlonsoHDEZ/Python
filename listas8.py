nombres = []
edades = []

while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad")))
    if nombre == "*": break

edad_max = max(edades)
print("Algunos mayores de edad")
print("========================")
for nombre,edad in zip(nombres,edades):
    if edad == edad_max:
        print(nombre)
    
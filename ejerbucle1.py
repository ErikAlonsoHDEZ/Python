resultado = 1;
num=int(input("Dime un número"))
contador = 2
while contador <= num:
    resultado = resultado * contador
    contador = contador + 1
print("El resultado es", resultado)
import random
def CalcularMaxMin(lista):
    return (max(lista),min(lista))

numeros = []

for i in range(10):
    numeros.append(random.randint(1,100))
vmax,vmin = CalcularMaxMin(numeros)
print("El valor máximo es",vmax)
print("El valor mínimo es",vmin)
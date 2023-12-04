suma = 0
cont = 0

num=int(input("Numero (0 para salir):"))
while num != 0:
    suma = suma + num
    cont = cont + 1
    num=int(input("Numero (0 para salir):"))
if cont > 0:
    media = suma / cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)
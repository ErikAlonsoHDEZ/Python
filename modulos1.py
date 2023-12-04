def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado*=i
    return resultado

num = int(input("Dame un número:"))
print(factorial(num))
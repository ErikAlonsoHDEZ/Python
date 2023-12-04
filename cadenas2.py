cad = input("Introduce una cadena:")
subcad = input("Introduce una subcadena")
if cad.startswith(subcad):
    print("La cadena comienza por subcadena")
else:
    print("La cadena NO comienza por subcadena")
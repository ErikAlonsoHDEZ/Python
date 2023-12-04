cad=input("Dime un número")
try:
    print (10/int(cad))
except ValueError:
    print("No se puedeconvertir a entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Se ha producido otro error")
finally:
    print("Se ejecuta siempre al finalizar")
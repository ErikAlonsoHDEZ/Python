usuario = input("Introduce el usuario:")
password = input("Introduce el password:")
if usuario == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    if usuario == "pepe" and password != "asdasd":
        print("Password incorrecto")
    else:
        print("Usuario/Password incorrecto")
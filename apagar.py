#!/usr/bin/python3

import sys,os

opcion = ""
while opcion < "a" or opcion > "c":
    print("a, Cerrar sesión")
    print("b, Apagar el sistema")
    print("c, Reinicar el sistema")
    opcion=input("Elija una opción:").lower()

#if opcion == "a":
 #   print("Cerrando la sesión")
  #  # os.system
#elif opcion == "b":
 #   print("Apagando el sistema")
#else:
    #print("Reiniciando el sistema")


match opcion:
    case "a":
        print("Cerrar sesión")
    case "b":
        print("Apagando el sistema")
    case "c":
        print("Reiniciando el sistema")
#!/usr/bin/python3
import sys

script=sys.argv[0]
params=sys.argv[1:]

if len(params) != 3:
    print("El número de parametros no es correcto")
    exit(1)

# convertir los parametos en enteros
for i in range(0, len(params)):
    params[i]=int(params[i])

# busco el mayor
mayor=param[0]
for i in range(1, len(params)):
    if params[i] > mayor:
        mayor = params[i]

# muestro el mayor
print(mayor, "es el mayor")
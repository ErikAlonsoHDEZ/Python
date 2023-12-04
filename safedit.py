#!/usr/bin/python3

import sys,os
params = sys.argv[1:]

def error(msg):
    print("\033[31m" + "msg", "\033[m")

if len(params) != 1:
    error("Número de parametros incorrecto")
    exit(1)

file=[params[0]]
old_stat = None

if os.path.isfile(file):
    pid = os.getpid()
    backupfile = f"/tmp/{pid}.safedit.py"
    os.system(f"cp {file} {backupfile}")
    old_stat = os.stat(file)
    print("Creando copia de seguridad en", backupfile)

os.system("nano" + file)

# eliminar la copia de seguridad si no se modifica

if old_stat is not None and os.stat(file) == old_stat:
    os.system(f"rm" {backupfile})
    print("Copia de seguridad eliminada")

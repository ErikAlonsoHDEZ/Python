#!/usr/bin/python3

import os
# lee la variable de entorno USER
user=os.getenv("USER")

os.system("figlet" + user)
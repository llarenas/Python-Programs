#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Know your PC — The machine settings.

Developed by Ronel Llarenas (https://github.com/llarenas/)
"""

import os
os.system("clear")
print (" _____                                     _____ _____ ")
print ("|  |  |___ ___ _ _ _    _ _ ___ _ _ ___   |  _  |     |")
print ("|    <    | . | | | |  | | | . | | |  _|  |   __|   --|")
print ("|__|__|_|_|___|_____|  |_  |___|___|_|    |__|  |_____|")
print ("                       |___| Developed by Ronel Llarenas     ")
print ("KNOW YOUR PC:\n")

print ("[ Name of Machine: ]")
os.system("uname -n\n")

print ("\n[ name Kernel: ]")
os.system("uname -s")

print ("\n[ Versin of Kernel: ]")
os.system("uname -v")
os.system("uname -r")

print ("\n[ OS: ]")
os.system("uname -o")

print ("\n[ Hardware of this machine: ]")
os.system("uname -m")

print ("\n[ Procesor: ]")
os.system("uname -p")

print ("\n[ Platform of Hardware: ]" )
os.system("uname -i")

# Enjoy!!!

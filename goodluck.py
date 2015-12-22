#!/usr/bin/python
# coding: utf-8

"""
Good Luck or Not. — Developed by Ronel Llarenas.
$  https://github.com/llarenas/
"""

import random
import time

sorte	=	["yes", "nope"]

print ("Good luck... or not.\n\n")
time.sleep(6.5)
if (random.choice(sorte)) == sorte[0]: #if random the string in array go to 0 means yes
	print ("You're in luck!")
else:
	print ("You're outta luck.")



 #!/bin/python

"""
Written by Ronel Llarenas.
"""

# Colours
D  = "\033[0m";  
W  = "\033[01;37m";  
O  = "\033[01;33m"; 
SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";

import socket
import sys
import os
os.system("clear")
print ( "+----------------------------------------------------------------------------+")
print ("|                                      DNSMap                                |")
print ("+----------------------------------------------------------------------------+")
print ("|                            Development by Ronel B. Llarenas.                       |")
print ("|                         $ Wget > http://github.com/llarenas                    |")
print( "+----------------------------------------------------------------------------+")
print (W+"")
domain = input("Set domain: ") # www.domain.com
 
try:
    ip = socket.gethostbyname( domain )
 
except socket.gaierror:
    print (FAIL+'Invalid Domain.\n\n\n\n\n\n\n')
    sys.exit()
print (SUCESS+"+-------------------------+")
print (SUCESS+"| DNS   : " +ip+ "     |")
print (SUCESS+"+-------------------------+")

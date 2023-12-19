#figlet

from pyfiglet import Figlet
import random
import sys

#TO use module
figlet = Figlet()

#Check Errors
if len(sys.argv) not in [1,3]:
    print("ERROR por len")
    sys.exit("Invalid usage")
    if sys.argv[1] not in ["-f","--font"]:
        print("ERROR por 1 arg")
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        print("ERROR por 2 arg")
        sys.exit("Invalid usage")

print("Ejecucion sin errores")
print(type (sys.argv[1]))
print(sys.argv[1] == "-f")
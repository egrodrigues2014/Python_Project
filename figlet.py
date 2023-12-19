#figlet

from pyfiglet import Figlet
import random
import sys

#TO use module
figlet = Figlet()

#Check Errors
if len(sys.argv) not in [1,3] or sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid usage")

#User input
s = input("Input:")

if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
    print("Output:",figlet.renderText(s))

else:
    r= random.choice(figlet.getFonts())
    figlet.setFont(font=r)
    print("Output:",figlet.renderText(s))




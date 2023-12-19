#Adieu, Adieu

import inflect
p = inflect.engine()

list_names = ["Elton","Ale","Tai"]

print(f"Adieu,adieu,to {p.join(list_names)}")


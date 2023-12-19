#Adieu, Adieu

import inflect
p = inflect.engine()

list_names = []

while True:
    try:
        name = input("Name:")
    except EOFError:
        #Validate if List is not empty
        if list_names:
            print(f"Adieu,adieu,to {p.join(list_names)}")
        break
    else:
        list_names.append(name)

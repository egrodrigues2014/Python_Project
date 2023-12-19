#Fuel Gauge

while True:
    gas = input("Fraction:")
    try:
        x,y = gas.split('/')
        result= int(x)/int(y)
        if result > 1:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if result <= 0.01:
    print("E")
elif result >= 0.99:
    print("F")
else:
    print(f"{int(result*100)}%")
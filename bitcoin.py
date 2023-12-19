import requests
import json
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    #print(json.dumps(r.json(), indent=2))

    o = r.json()
    rate = o["bpi"]["USD"]["rate"].replace(",", "")
    # print(rate)
    # print(type(sys.argv[1]))
    try:
        amount = float(rate) * float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()

    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit()

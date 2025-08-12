import requests
import sys

try:
    if sys.argv != 1:
        try:
            num = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()

for result in o:
    a = o["bpi"]
for c in a["USD"]:
    b = a["USD"]
rate = b["rate_float"]*num

print(f"${rate:,.4f}")
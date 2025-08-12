import sys
import csv
from tabulate import tabulate

try:
    menu = []

    if len(sys.argv) == 2:
        if f"{sys.argv[1]}".endswith(".csv") == False:
            sys.exit("Not a CSV file")
        else:
            with open(f"{sys.argv[1]}") as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(row)
            print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

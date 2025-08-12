import sys

try:
    i = 0
    if len(sys.argv) == 2:
        if f"{sys.argv[1]}".endswith(".py") == False:
            sys.exit("Not a Python file")
        else:
            with open(f"{sys.argv[1]}") as file:
                for line in file:
                    if line.strip() == "" or line.lstrip().startswith("#"):
                        continue
                    else:
                        i += 1
        print(i)
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

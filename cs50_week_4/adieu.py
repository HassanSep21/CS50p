import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").capitalize()
        names.append(name)
    except EOFError:
        print()
        break
names = p.join(names)

print(f"Adieu, adieu, to {names}")
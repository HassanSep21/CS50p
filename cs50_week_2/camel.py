camel = input("camelCase: ")
while True:
    print("sanke_case: ", end="")
    for letter in camel:
        if letter.islower():
            print(letter, end="")
        else:
            letter = letter.lower()
            print(f"_{letter}", end="")
    break
print()
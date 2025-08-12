cart = []
i = 0
while True:
    try:
        item = input()
        cart.append(item)
    except EOFError:
        print()
        break
cart.sort()
for food in cart:
    if food in cart[:i]:
        pass
    else:
        count = cart.count(food)
        print(f"{count} {food.upper()}")
    i += 1

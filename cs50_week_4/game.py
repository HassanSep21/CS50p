from random import randint

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            num = randint(1, lvl)
            break
        else:
            pass
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > num:
                print("Too large!")
                pass
            elif guess < num:
                print("Too small!")
                pass
            else:
                print("Just right!")
                break
        else:
            pass
    except ValueError:
        pass

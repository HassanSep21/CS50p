import random


def main():

    count = 0
    score = 0

    level = get_level()
    while True:
        tries = 1
        if count != 10:
            x = generate_integer(level)
            y = generate_integer(level)
            while True:
                ans = int(input(f"{x} + {y} = "))
                if ans == x+y:
                    score += 1
                    count += 1
                    break
                else:
                    if tries == 3:
                        print(f"{x} + {y} = {x+y}")
                        count += 1
                        break
                    else:
                        print("EEE")
                        tries += 1
                        pass
        else:
            break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n <= 3:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
        return num
    elif level == 2:
        num = random.randint(10, 99)
        return num
    elif level == 3:
        num = random.randint(100, 999)
        return num
    else:
        raise ValueError

if __name__ == "__main__":
    main()
def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
    if 2 <= len(s) <=6 and s[0:2].isalpha() and s.isalnum():
        for ch in s:
            if ch.isdigit():
                index = s.index(ch)
                if s[index:].isdigit() and int(ch) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
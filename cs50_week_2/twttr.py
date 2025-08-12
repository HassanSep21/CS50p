def main():
    txt = input("Input: ")
    print(shorten(txt))



def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text = ""
    for letter in word:
        if letter in vowels:
            continue
        else:
            text = text + letter
    return text


if __name__ == "__main__":
    main()
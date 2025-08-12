import os
import sys
from PIL import Image
from PIL import ImageOps

def main():

    if len_arg(len(sys.argv)):
        file1 = os.path.splitext(sys.argv[1])
        file2 = os.path.splitext(sys.argv[2])
        if extension(file1[1], file2[1]):
            try:
                shirt = Image.open("shirt.png")
                image = Image.open(sys.argv[1])
                size1 = shirt.size
                image = ImageOps.fit(image, size1)
                image.paste(shirt, (0, 0), mask=shirt)
                image.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit("Input does not exist")

def len_arg(z):
    if z == 3:
        return True
    elif z > 3:
        sys.exit("Too many command-line argumnets")
    else:
        sys.exit("Too few command-line argmunets")


def extension(x, y):
    exes = [".png", ".jpg", ".jpeg"]
    if x in exes and y in exes:
        pass
    else:
        sys.exit("Invalid Output")
    if x == y:
        return True
    else:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
import pyfiglet
import random
import sys

figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()

if len(sys.argv) > 1:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        text = input("Input: ")
        font = figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(text))
